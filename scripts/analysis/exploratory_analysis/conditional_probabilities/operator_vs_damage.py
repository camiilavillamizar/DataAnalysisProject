
from analysis.exploratory_analysis.conditional_probabilities.common_imports_conditional_probabilities import pd, plot

def getConditionalProbabilitiesOperatorVSDamage(df): 
    filtered_df = df[df["OperatorTypeID_DisplayEng"] != "UNKNOWN"]
    filtered_df = filtered_df[filtered_df['DamageLevelID_DisplayEng'] != "UNKNOWN"]
    joint_prob = pd.crosstab(
        filtered_df['OperatorTypeID_DisplayEng'],
        filtered_df['DamageLevelID_DisplayEng'],
        normalize='index'  
    )

    #Heatmap
    plot(joint_prob, "Conditional Probability: Operator Type vs Damage Level (Rows Sum to 1)")
