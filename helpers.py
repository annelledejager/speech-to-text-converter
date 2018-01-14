import json
import pyaudio
import requests
from snowboy import snowboydecoder

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

URL = 'https://api.wit.ai/speech?v=20170307'
WIT_ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

HOT_WORD = 'dolphin'

NUM_OF_CHARS_PER_LINE = 120


def convert_speech_to_text(audio):
    headers = {
        'Authorization': 'Bearer ' + WIT_ACCESS_TOKEN,
        'Content-Type': 'audio/wav',
    }

    response = requests.post(URL, data=audio, headers=headers)

    data = json.loads(response.content)
    return data.get('_text')


def cleanup_text(text):
    # cleanup commas, full stops and I's
    text = text.replace('comma', ', ')
    text = text.replace(' ,', ',')
    text = text.replace('full stop', '.')
    text = text.replace(' .', '.')
    text = text.replace('i ', 'I ')
    text = text.replace(HOT_WORD, '')
    return text


def write_text_to_file(text):
    cleaned_text = cleanup_text(text)
    with open('output.txt','a') as f:
        i = 0
        while i <= len(cleaned_text):
            f.write(cleaned_text[i:i+NUM_OF_CHARS_PER_LINE] + '\n')
            i = i + NUM_OF_CHARS_PER_LINE

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
