# audio/narrator.py

from gtts import gTTS
import os
import datetime

def convert_text_to_speech(text, lang='en'):
    filename = f"cartoon_story_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    return filename
