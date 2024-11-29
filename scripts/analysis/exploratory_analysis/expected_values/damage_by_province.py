from analysis.exploratory_analysis.expected_values.plot_expected_values import plot
from analysis.exploratory_analysis.constants_exploratory_analysis import DAMAGE_MAPPING

def plotDamageByProvince(df): 

    df['DamageLevelNumeric'] = df['DamageLevelID_DisplayEng'].map(DAMAGE_MAPPING)

    #11 most frequent provinces
    top_11_provinces = df['ProvinceID_DisplayEng'].value_counts().nlargest(11).index

    #Filter data for the top 11 provinces
    filtered_df = df[df['ProvinceID_DisplayEng'].isin(top_11_provinces)].copy()

    #Calculate the expected damage level for each province
    expected_damage_province = filtered_df.groupby('ProvinceID_DisplayEng')['DamageLevelNumeric'].mean()
    print(expected_damage_province)

    plot(expected_damage_province, 
         "Expected Damage Level by Province (Top 11 Provinces)", 
         "Expected Damage Level (Numeric)", 
         "Province")
