
from analysis.exploratory_analysis.marginal_probabilities.common_imports_marginal_probabilities import pd, SELECTED_PROVINCES, plot


def plotMarginalProbabilitiesOfOperartorByProvince(province_probabilities):
    operator_types = pd.DataFrame(province_probabilities['OperatorTypeID_DisplayEng'].tolist(),
                               index=province_probabilities.index).fillna(0)

    #Just Canadian provinces
    operator_types.index = operator_types.index.str.upper()
    operator_types_filtered = operator_types.loc[operator_types.index.intersection(SELECTED_PROVINCES)]

    operator_types_filtered = operator_types_filtered.drop(columns=['UNKNOWN', 'OTHER'])
        
    #Graph
    plot(operator_types_filtered, 
         "Marginal Probability of Each Type of Operator in a Specific Province", 
         "Proportion", 
         "Province", 
         "Operator Type")

    return operator_types_filtered