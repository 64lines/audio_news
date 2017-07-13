import os
import random
from datetime import datetime as date

def get_voice():
    # "Samantha"
    return "Tessa"

def run_voice_command(text, voice):
    return os.system("say \"%s\" --voice=%s" % (text.encode('utf-8'), voice))

def say_text(text):
    return run_voice_command(text, get_voice())

def get_hour():
    return date.now().hour

def is_morning():
    return get_hour() < 12

def is_afternoon():
    return 12 <= get_hour() < 18

def calculate_gretting_text():
    return "Good morning" if is_morning() else "Good afternoon" if is_afternoon() else "Good evening"

def greeting():
    return run_voice_command(calculate_gretting_text(), get_voice())
