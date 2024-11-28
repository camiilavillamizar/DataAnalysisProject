
from analysis.exploratory_analysis.marginal_probabilities.common_imports_marginal_probabilities import pd, SELECTED_PROVINCES, plot

def plotMarginalProbabilitiesOfAircraftByProvince(province_probabilities):
    aircraft_types = pd.DataFrame(province_probabilities['AircraftTypeID_DisplayEng'].tolist(),
                              index=province_probabilities.index).fillna(0)

    aircraft_types.index = aircraft_types.index.str.upper()
    aircraft_types_filtered = aircraft_types.loc[aircraft_types.index.intersection(SELECTED_PROVINCES)]
    aircraft_types_filtered = aircraft_types_filtered.drop(columns=['UNKNOWN'])

    #Graph
    plot(aircraft_types_filtered, 
         "Marginal Probability of Each Aircraft Type in a Specific Province", 
         "Proportion", 
         "Province", 
         "Aircraft Type"
         )

    return aircraft_types_filtered

def plotWithoutFirst2(aircraft_types_filtered):
    aircraft_types_filtered = aircraft_types_filtered.drop(columns=['AEROPLANE','HELICOPTER'])
    plot(aircraft_types_filtered, 
         "Marginal Probability of Each Aircraft Type in a Specific Province Without first 2 Types", 
         "Proportion", 
         "Province", 
         "Aircraft Type"
        )

    return aircraft_types_filtered