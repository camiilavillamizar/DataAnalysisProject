
import pandas as pd
from preprocessing.translations.check_french import is_french
from preprocessing.translations.trans_french_to_eng import translate_to_english
from preprocessing.translations.translation_constants import COLUMNS_TO_TRANSLATE
from common.export_temp_csv import export_csv_temp


def process_translation(df):
    
    df_filtered = df[["OccID", "Summary"]].copy()

    for column in COLUMNS_TO_TRANSLATE:
        df_filtered[column] = df_filtered[column].apply(
            lambda x: translate_to_english(x) if is_french(str(x)) else x
        )
    
    export_csv_temp(df_filtered, "eng_summaries")
    


