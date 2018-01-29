from gtts import gTTS
import subprocess
import time
import platform
import logging

AUDIO_FILE = time.strftime("crawler_af_%d%h%Y_%H%M%S.mp3")
LANGUAGE_LITERAL = 'ipx_lang:'

logger = logging.getLogger("ipx_logger")


def speak(speech, language):
    text_to_speech = gTTS(text=speech, lang=language)
    text_to_speech.save(AUDIO_FILE)
    if platform.system() == 'Windows':
        os_cmd = AUDIO_FILE
    elif platform.system() == 'Linux':
        os_cmd = 'mpg321 ' + AUDIO_FILE
    else:
        os_cmd = AUDIO_FILE

    os_cmd = os_cmd.split()
    subprocess.call(os_cmd, shell=True)


def speak_obsolete(speech, language):
    if platform.system() == 'Windows':
        text_to_speech = gTTS(text=speech, lang=language)
        text_to_speech.save(AUDIO_FILE)
        os_cmd = AUDIO_FILE
    elif platform.system() == 'Linux':
        os_cmd = 'espeak ' + "\"" + speech + "\""

    # os_cmd = os_cmd.split()
    subprocess.call(os_cmd, shell=True)


