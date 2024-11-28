from analysis.exploratory_analysis.conditional_probabilities.common_imports_conditional_probabilities import pd, plot

def getConditionalProbabilitiesTop10CommercialOrganizationsVSDamage(df):
    filtered_df = df[
    (df['OperatorTypeID_DisplayEng'] == "COMMERCIAL") &
    (df['OrganizationID_DisplayEng'] != "UNKNOWN")
    ]
    filtered_df = filtered_df[filtered_df['DamageLevelID_DisplayEng'] != "UNKNOWN"]
    top_10_organizations = (
        filtered_df['OrganizationID_DisplayEng']
        .value_counts()
        .head(15)
        .index
    )

    filtered_df = filtered_df[
        (filtered_df['OrganizationID_DisplayEng'].isin(top_10_organizations))
    ]
    joint_prob = pd.crosstab(
        filtered_df['OrganizationID_DisplayEng'],
        filtered_df['DamageLevelID_DisplayEng'],
        normalize='index'
    )

    plot(joint_prob, "Conditional Probability: Top 10 Commercial organizations vs Damage Level")
