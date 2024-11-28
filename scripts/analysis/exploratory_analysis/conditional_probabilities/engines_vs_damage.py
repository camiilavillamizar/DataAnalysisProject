from analysis.exploratory_analysis.conditional_probabilities.common_imports_conditional_probabilities import pd, plot
def getConditionalProbabilitiesEnginesVSDamage(df):
    filtered_df = df[df['NumberOfEngine'].isin([1, 2, 3, 4, 5, 6, 7, 8])]
    filtered_df = filtered_df[filtered_df['DamageLevelID_DisplayEng'] != "UNKNOWN"]

    joint_prob = pd.crosstab(
        filtered_df['NumberOfEngine'],
        filtered_df['DamageLevelID_DisplayEng'],
        normalize='index'    
    )

    plot(joint_prob, "Conditional Probability: Number of Engines vs Damage Level (Rows sum 1)")