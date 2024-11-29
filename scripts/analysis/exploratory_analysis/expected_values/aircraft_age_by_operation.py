from analysis.exploratory_analysis.expected_values.plot_expected_values import plot
import pandas as pd

def plotAircraftAgeByOperation(df): 
    #Filtering out unknown and other operation types
    filtered_df = df[(df["OperationTypeID_DisplayEng"] != "UNKNOWN") & (df["OperationTypeID_DisplayEng"] != "OTHER")].copy()

    #Calculate aircraft age 
    filtered_df.loc[:, 'AircraftAge'] = pd.to_datetime(filtered_df['OccDate']).dt.year - filtered_df['YearOfManuf']

    #Calculating the expected aircraft age for each operation type
    expected_age = filtered_df.groupby('OperationTypeID_DisplayEng')['AircraftAge'].mean()

    print(expected_age)
    plot(expected_age, 
         "Expected Aircraft Age by Operation Type", 
         "Expected Aircraft Age (Years)", 
         "Operation Type")
