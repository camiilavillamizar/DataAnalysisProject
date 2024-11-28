
from analysis.exploratory_analysis.marginal_probabilities.common_imports_marginal_probabilities import  plot

def plotMarginalProbabilitiesOfOccurrenceByProvince(province_probabilities):
    incident_probabilities = province_probabilities['IncidentCount'] / province_probabilities['IncidentCount'].sum()

    #Showing most frequent provinces
    threshold = 0.01 / incident_probabilities.sum()
    filtered_province_probabilities = incident_probabilities[incident_probabilities > threshold]

    plot(filtered_province_probabilities, 
         "Probability of Accidents by Province", 
         "Province",
         "Probability (%)"
         )

    filtered_province_probabilities_df = filtered_province_probabilities.reset_index()
    return filtered_province_probabilities_df