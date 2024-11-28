
from analysis.exploratory_analysis.marginal_probabilities.common_imports_marginal_probabilities import pd, SELECTED_PROVINCES, plot


def plotMarginalProbabilitiesOfOperartionByProvince(province_probabilities):
    operation_types = pd.DataFrame(province_probabilities['OperationTypeID_DisplayEng'].tolist(),
                               index=province_probabilities.index).fillna(0)

    operation_types.index = operation_types.index.str.upper()
    operation_types_filtered = operation_types.loc[operation_types.index.intersection(SELECTED_PROVINCES)]

    operation_types_filtered = operation_types_filtered.drop(columns=['UNKNOWN', 'OTHER'])
        
    
    plot(operation_types_filtered,
         "Marginal Probability of Each Type of Operation in a Specific Province",
         "Proportion",
         "Province", 
         "Operation Type")

    return operation_types_filtered

def plotWithoutFirstTwoOperations(province_probabilities):
    operation_types = pd.DataFrame(province_probabilities['OperationTypeID_DisplayEng'].tolist(),
                               index=province_probabilities.index).fillna(0)

    operation_types.index = operation_types.index.str.upper()
    operation_types_filtered = operation_types.loc[operation_types.index.intersection(SELECTED_PROVINCES)]
    operation_types_filtered = operation_types_filtered.drop(columns=['UNKNOWN', 'OTHER', 'AIR TRANSPORT', 'PLEASURE/TRAVEL'])
        
    plot(operation_types_filtered,
        "Marginal Probability of Each Type of Operation in a Specific Province Excluding air transport and pleasure",
        "Proportion",
        "Province", 
        "Operation Type")

    return operation_types_filtered