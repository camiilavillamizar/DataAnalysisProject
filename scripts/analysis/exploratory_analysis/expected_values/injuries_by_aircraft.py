from analysis.exploratory_analysis.expected_values.plot_expected_values import plot

def plotInjuriesByAircraft(df): 
    #Injuries to numeric values
    injury_mapping = {'No': 0, 'Yes': 1}
    filtered_df = df[df["AircraftTypeID_DisplayEng"] != "UNKNOWN"].copy()
    filtered_df['InjuryNumeric'] = filtered_df['InjuriesEnum_DisplayEng'].map(injury_mapping)

    #Calculating the expected number of injuries for each aircraft type
    expected_injuries = filtered_df.groupby('AircraftTypeID_DisplayEng')['InjuryNumeric'].mean()
    print(expected_injuries)

    plot(expected_injuries, 
         "Expected Number of Injuries by Aircraft Type", 
         "Expected Number of Injuries", 
         "Aircraft Type")
