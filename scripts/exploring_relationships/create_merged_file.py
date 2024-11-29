import pandas as pd
from analysis.exploratory_analysis.constants_exploratory_analysis import SELECTED_PROVINCES
from common.export_csv import exportDataVersion


def createFileWithMergedDatasets(occurrences_df, passenger_traffic, dollar_df, births_df):
    occurrences_df = occurrences_df[occurrences_df['ProvinceID_DisplayEng'].str.upper().isin(SELECTED_PROVINCES)].copy()

    # Reset the index of the filtered DataFrame (optional)
    occurrences_df.reset_index(drop=True, inplace=True)

    # Creating new column to store year and month in occurrences_df
    occurrences_df['OccDate'] = pd.to_datetime(occurrences_df['OccDate'])
    occurrences_df['YearMonth'] = occurrences_df['OccDate'].dt.to_period('M')

    # Counting the number of occurrences per year-month
    occurrences_count = occurrences_df.groupby('YearMonth').size().reset_index(name='occurrences')

    # Preparing dollar exchange rate data
    dollar_df = dollar_df.melt(var_name="YearMonth", value_name="dollar_exchange")
    dollar_df['YearMonth'] = pd.to_datetime(dollar_df['YearMonth'], format='%b-%y').dt.to_period('M')

    # Preparing birth rate data
    births_df = births_df.melt(id_vars="Unnamed: 0", var_name="Year", value_name="births")
    births_df.rename(columns={'Unnamed: 0': 'Month'}, inplace=True)
    births_df['YearMonth'] = pd.to_datetime(births_df['Year'] + '-' + births_df['Month'], format='%Y-%B').dt.to_period('M')

    # Preparing passenger traffic data
    filtered_df = passenger_traffic[
        (passenger_traffic['GEO'] == 'Total of eight largest airports, Canada') &
        (passenger_traffic['Screened traffic'] == 'Total screened traffic')
    ].copy()

    filtered_df['REF_DATE'] = pd.to_datetime(filtered_df['REF_DATE'], format='%b-%y')
    filtered_df['YearMonth'] = filtered_df['REF_DATE'].dt.to_period('M')

    # Grouping passenger traffic by YearMonth and summing up the values
    passenger_traffic_sum = filtered_df.groupby('YearMonth')['VALUE'].sum().reset_index()
    passenger_traffic_sum.rename(columns={'VALUE': 'passenger_traffic'}, inplace=True)

    # Merging all data into a single DataFrame
    merged_df = pd.merge(occurrences_count, dollar_df, on="YearMonth", how="outer")
    merged_df = pd.merge(merged_df, births_df[['YearMonth', 'births']], on="YearMonth", how="outer")
    final_df = pd.merge(merged_df, passenger_traffic_sum, on="YearMonth", how="outer")

    # Sorting by YearMonth and resetting the index
    final_df['YearMonth'] = final_df['YearMonth'].astype(str)  # Converting to string yyyy-MM format
    final_df.sort_values(by='YearMonth', inplace=True)
    final_df.reset_index(drop=True, inplace=True)

    # Filtering the DataFrame to include only data between 1995-01 and 2023-12
    final_df['YearMonth'] = pd.to_datetime(final_df['YearMonth']).dt.to_period('M')
    start_date = pd.Period('1995-01', freq='M')
    end_date = pd.Period('2023-12', freq='M')

    final_df_filtered = final_df[(final_df['YearMonth'] >= start_date) & (final_df['YearMonth'] <= end_date)].copy()
    final_df_filtered.reset_index(drop=True, inplace=True)

    # Converting YearMonth back to string format
    final_df_filtered.loc[:, 'YearMonth'] = final_df_filtered['YearMonth'].astype(str)

    exportDataVersion(final_df_filtered, 3)