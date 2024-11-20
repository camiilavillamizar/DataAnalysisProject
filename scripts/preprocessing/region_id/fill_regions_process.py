import pandas as pd
from common.export_temp_csv import export_csv_temp
from preprocessing.region_id.region_by_coordinates import get_region_by_coordinates

def fill_regions_in_temp(df):
    df = pd.DataFrame(df)
    df_filtered = df[["OccID", "Latitude", "Longitude"]].copy()

    df_filtered["PROVINCE"] = df_filtered.apply(
    lambda row: get_region_by_coordinates(row["Latitude"], row["Longitude"]).upper(), axis=1
    )

    export_csv_temp(df_filtered, "null_provinces_filled")