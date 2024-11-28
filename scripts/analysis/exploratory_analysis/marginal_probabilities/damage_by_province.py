
from analysis.exploratory_analysis.marginal_probabilities.common_imports_marginal_probabilities import  ORDERED_DAMAGE_LEVELS, SELECTED_PROVINCES, plot

def plotMarginalProbabilitiesOfDamageByProvince(df):
    damage_levels = (
    df.groupby(['ProvinceID_DisplayEng', 'DamageLevelID_DisplayEng'])
    .size()
    .unstack(fill_value=0)  #Creating columns for each damage level
    .apply(lambda x: x / x.sum(), axis=1)  #Calculating proportions
    )
    damage_levels.index = damage_levels.index.str.upper()

    damage_levels_filtered = damage_levels.loc[damage_levels.index.intersection(SELECTED_PROVINCES)]
    if 'UNKNOWN' in damage_levels_filtered.columns:
        damage_levels_filtered = damage_levels_filtered.drop(columns=['UNKNOWN'])

    damage_levels_filtered = damage_levels_filtered[ORDERED_DAMAGE_LEVELS]

    #Graph
    plot(damage_levels_filtered, 
         "Marginal probability of each damage level in a specific province", 
         "Proportion", 
         "Province", 
         "Damage Level")

    return damage_levels_filtered