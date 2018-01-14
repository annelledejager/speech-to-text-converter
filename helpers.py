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
URL = 'https://api.wit.ai/speech?v=20170307'
WIT_TOKEN = 'LKGLMVPZYWHUIFT44G3NXTRXCL2JTHAV'


def convert_speech_to_text(audio):
    headers = {
        'Authorization': 'Bearer ' + WIT_TOKEN,
        'Content-Type': 'audio/wav',
    }

    response = requests.post(URL, data=audio, headers=headers)

    data = json.loads(response.content)
    return data.get('_text')


def write_text_to_file(text):
    words = text.split()
    words = filter(lambda a: a != 'dolphin', words)
    with open('output.txt','a') as f:
        i = 0
        while i < len(words):
            f.write(' '.join(words[i:i+20]) + '\n')
            i = i + 20

        f.write('\n')
    f.close()


def read_audio():
    with open(WAVE_OUTPUT_FILENAME, 'rb') as f:
        audio = f.read()

        f.close()
    return audio


def wait_for_hotword():
    detector = snowboydecoder.HotwordDetector('hotword.pmdl', sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    detector.start()
    detector.terminate()


def start_recording():
    detector = snowboydecoder.HotwordDetector('hotword.pmdl', sensitivity=0.5)
    detector.start(is_recording=True)
    detector.terminate()
