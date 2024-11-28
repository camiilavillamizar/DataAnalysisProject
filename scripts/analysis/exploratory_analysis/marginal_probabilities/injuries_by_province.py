
from analysis.exploratory_analysis.marginal_probabilities.common_imports_marginal_probabilities import pd, SELECTED_PROVINCES, plot


def plotMarginalProbabilitiesOInjuriesByProvince(province_probabilities):
    injuries_types = pd.DataFrame(province_probabilities['InjuriesEnum_DisplayEng'].tolist(),
                              index=province_probabilities.index).fillna(0)

    injuries_types.index = injuries_types.index.str.upper()
    injuries_types_filtered = injuries_types.loc[injuries_types.index.intersection(SELECTED_PROVINCES)]

    plot(injuries_types_filtered, 
         "Marginal Probability of Each Type of Injury in a Specific Province", 
         "Proportion", 
         "Province", 
         "Injury Type"
         )
    
    return injuries_types_filtered