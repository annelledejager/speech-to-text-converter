import json
import pyaudio
import requests
from snowboy import snowboydecoder
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"


class Recorder:
    def __init__(self):
        pass

    def start(self):
        with open(WAVE_OUTPUT_FILENAME, 'rb') as f:
            audio = f.read()

        f.close()

        headers = {
            'Authorization': 'Bearer LKGLMVPZYWHUIFT44G3NXTRXCL2JTHAV',
            'Content-Type': 'audio/wav',
        }

        url = 'https://api.wit.ai/speech?v=20170307'

        response = requests.post(url, data=audio, headers=headers)

        data = json.loads(response.content)

        text = data.get('_text')

        if text:
            words = text.split()
            words = filter(lambda a: a != 'dolphin', words)
            with open('output.txt','a') as f:
                i = 0
                while i < len(words):
                    f.write(' '.join(words[i:i+20]) + '\n')
                    i = i + 20

                f.write('\n')
            f.close()


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-c':
        open('output.txt', 'w').close()

    detector = snowboydecoder.HotwordDetector('hotword.pmdl', sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    detector.start()
    detector.terminate()

    detector = snowboydecoder.HotwordDetector('hotword.pmdl', sensitivity=0.5)
    detector.start(is_recording=True)
    detector.terminate()

    recorder = Recorder()
    recorder.start()
