from deep_translator import GoogleTranslator

def translate_to_english(french_text):
    try:
        return GoogleTranslator(source='fr', target='en').translate(french_text)
    except Exception as e:
        return french_text  # Return original text in case of error
