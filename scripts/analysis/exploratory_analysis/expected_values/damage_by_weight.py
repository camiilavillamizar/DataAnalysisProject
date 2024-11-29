from analysis.exploratory_analysis.expected_values.plot_expected_values import plot
from analysis.exploratory_analysis.constants_exploratory_analysis import DAMAGE_MAPPING

def plotDamageByWeight(df):
    df['DamageLevelNumeric'] = df['DamageLevelID_DisplayEng'].map(DAMAGE_MAPPING)
    filtered_df = df[df["WeightCategoryID_DisplayEng"] != "UNKNOWN"]

    expected_damage = filtered_df.groupby('WeightCategoryID_DisplayEng')['DamageLevelNumeric'].mean()
    print(expected_damage)
    plot(expected_damage, 
         "Expected Damage Level by Weight Category", 
         "Expected Damage Level (Numeric)", 
         "Weight Category")
