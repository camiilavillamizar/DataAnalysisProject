from analysis.exploratory_analysis.conditional_probabilities.common_imports_conditional_probabilities import pd, plot

def getConditionalProbabilitiesTop10ManufacturersVSDamage(df):
    #10 most frecuent fabricants
    top_10_aircraft_makes = (
        df['AircraftMakeID_DisplayEng']
        .value_counts()
        .head(10)
        .index
    )

    filtered_df = df[
        (df['AircraftMakeID_DisplayEng'].isin(top_10_aircraft_makes)) &
        (df['AircraftMakeID_DisplayEng'] != "UNKNOWN MANUFACTURER")
    ]
    filtered_df = filtered_df[filtered_df['DamageLevelID_DisplayEng'] != "UNKNOWN"]

    joint_prob = pd.crosstab(
        filtered_df['AircraftMakeID_DisplayEng'],
        filtered_df['DamageLevelID_DisplayEng'],
        normalize='index'
    )

    plot(joint_prob, "Conditional Probability: Top 10 Aircraft Makes vs Damage Level")
