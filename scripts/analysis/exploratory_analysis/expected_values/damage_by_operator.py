from analysis.exploratory_analysis.expected_values.plot_expected_values import plot

def plotDamageByOperator(df): 
    #Calculating the expected damage level for each operator type
    filtered_df = df[(df["OperatorTypeID_DisplayEng"] != "UNKNOWN") & (df["OperatorTypeID_DisplayEng"] != "OTHER")].copy()
    expected_damage_operator = filtered_df.groupby('OperatorTypeID_DisplayEng')['DamageLevelNumeric'].mean()
    print(expected_damage_operator)

    plot(expected_damage_operator, 
         "Expected Damage Level by Operator Type", 
         "Expected Damage Level (Numeric)", 
         "Operator Type")
