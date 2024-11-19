
from googletrans import Translator

translator = Translator()

def translate_to_english(french_text):
    try:
        return translator.translate(french_text, src="fr", dest="en").text
    except Exception as e:
        return french_text  # Return original text in case of error
