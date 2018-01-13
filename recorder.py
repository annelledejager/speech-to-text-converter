import json
import wave
import pyaudio
import requests
from snowboy import snowboydecoder

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
        # p = pyaudio.PyAudio()
        #
        # stream = p.open(format=FORMAT,
        #                 channels=CHANNELS,
        #                 rate=RATE,
        #                 input=True,
        #                 frames_per_buffer=CHUNK)
        #
        # print("Recording...")
        #
        # frames = []
        #
        # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        #     data = stream.read(CHUNK)
        #     frames.append(data)
        #
        # print("Done recording!")
        #
        # stream.stop_stream()
        # stream.close()
        # p.terminate()

        # wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        # wf.setnchannels(CHANNELS)
        # wf.setsampwidth(2)
        # wf.setframerate(RATE)
        # wf.writeframes(b''.join(self.frames))
        # wf.close()

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
        print text

        if text:
            words = text.split()
            with open('output.txt','w') as f:
                i = 0
                while i < len(words):
                    f.write(' '.join(words[i:i+15]) + '\n')
                    i = i + 1

            f.close()


if __name__ == '__main__':
    detector = snowboydecoder.HotwordDetector('hotword.pmdl', sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    detector.start()
    detector.terminate()

    recorder = Recorder()
    recorder.start()
