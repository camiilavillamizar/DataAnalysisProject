
import pandas as pd
from preprocessing.translations.check_french import is_french
from preprocessing.translations.trans_french_to_eng import translate_to_english
from preprocessing.translations.translation_constants import COLUMNS_TO_TRANSLATE


def process_translation(df):
    
    for column in COLUMNS_TO_TRANSLATE:
        df[column] = df[column].apply(
            lambda x: translate_to_english(x) if is_french(str(x)) else x
        )

