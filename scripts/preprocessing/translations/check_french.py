
from langdetect import detect

def is_french(text):
    try:
        return detect(text) == "fr"
    except:
        return False
