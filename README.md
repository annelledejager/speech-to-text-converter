# speech to text converter

A python client for interacting with Wit Speech Recognition API to convert speech to text.

## Getting the code

Clone the repository normally 

```
git clone git@github.com:annelledejager/speech-to-text-converter.git
```

### Prerequisites

* [Pysox](https://github.com/rabitt/pysox) 

    To install SoX on Mac with Homebrew:
    
    ```
    brew install sox
    ```
    
    To install the most up to date release of this module via PyPi:
    
    ```
    pip install sox
    ```
    
    To install the master branch:
    
    ```
    pip install git+https://github.com/rabitt/pysox.git
    ```
* [Snowboy](http://docs.kitt.ai/snowboy/)

Create a hotword on Snowboy and download its .pmdl file. You can also use an existing one. Replace the[.pmdl](https://github.com/annelledejager/speech-to-text-converter/blob/master/hotword.pmdl) file. 

The current hotword used in the project is 'dolphin'.

* [Wit](http://wit.ai/)

Create an account in order to retrieve a Wit access token.

### Using the speech converter

The converter waits for the hotword to start recording. It then records until the hotword is detected again. It then does the conversion from speech to text. 

The output text is written to an output.txt file. It appends the recordings on new lines. 
```
python speech_to_text_converter.py
```
The converter allows input flag `-c` to clean the output.txt before the next recording. 
```
python speech_to_text_converter.py -c  
```

Example output
```
Listening... Press Ctrl+C to exit
INFO:snowboy:Keyword 1 detected at time: 2018-01-14 11:10:28
INFO:snowboy:Keyword 1 detected at time: 2018-01-14 11:10:38
Speech converted to text. Please see output.txt.
```

## Built With

* [Snowboy](http://docs.kitt.ai/snowboy/) - a Customizable Hotword Detection Engine
* [Wit](http://wit.ai/) - Natural Language for Developers

