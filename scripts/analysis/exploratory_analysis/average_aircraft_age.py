
from analysis.exploratory_analysis.marginal_probabilities.common_imports_marginal_probabilities import SELECTED_PROVINCES, plt

def plotAverageAircraftAge(province_probabilities):
    #Filtering average year 
    aircraft_age = province_probabilities['YearOfManuf']

    #Filtering selected provinces
    aircraft_age.index = aircraft_age.index.str.upper()
    aircraft_age_filtered = aircraft_age.loc[aircraft_age.index.intersection(SELECTED_PROVINCES)]

    #Graph
    aircraft_age_filtered.plot(kind='bar', figsize=(10, 6), color='#80549c', edgecolor='black')
    plt.title('Average Age of Aircraft Involved in Incidents in a Specific Province')
    plt.ylabel('Average Year of Manufacture')
    plt.xlabel('Province')
    plt.xticks(rotation=45)
    plt.ylim(1970, 1990)  
    plt.yticks(range(1970, 1990, 2))
    plt.tight_layout()
    plt.show()

    aircraft_age_filtered_df = aircraft_age_filtered.reset_index()
    return aircraft_age_filtered_df