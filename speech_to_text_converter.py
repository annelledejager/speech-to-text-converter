import sys
from helpers import read_audio, convert_speech_to_text, write_text_to_file, wait_for_hotword, start_recording


class SpeechToTextConverter:
    def __init__(self):
        pass

    @staticmethod
    def convert_speech_to_text():
        audio = read_audio()

        text = convert_speech_to_text(audio)

        if text:
            write_text_to_file(text)
            print('Speech converted to text. Please see output.txt.')
        else:
            print('No speech detected.')


def cleanup():
    open('output.txt', 'w').close()


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-c':
        cleanup()

    wait_for_hotword()
    start_recording()

    converter = SpeechToTextConverter()
    converter.convert_speech_to_text()
