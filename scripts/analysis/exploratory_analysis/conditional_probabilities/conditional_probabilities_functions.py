from analysis.exploratory_analysis.conditional_probabilities.engines_vs_damage import getConditionalProbabilitiesEnginesVSDamage
from analysis.exploratory_analysis.conditional_probabilities.operator_vs_damage import getConditionalProbabilitiesOperatorVSDamage
from analysis.exploratory_analysis.conditional_probabilities.top10_manufacturers_vs_damage import getConditionalProbabilitiesTop10ManufacturersVSDamage
from analysis.exploratory_analysis.conditional_probabilities.top10_manufacturers_vs_injuries import getConditionalProbabilitiesTop10ManufacturersVSInjuries
from analysis.exploratory_analysis.conditional_probabilities.top10_commercial_organizations_vs_damage import getConditionalProbabilitiesTop10CommercialOrganizationsVSDamage

def getEngineVSDamege(df):
    getConditionalProbabilitiesEnginesVSDamage(df)

def getOperatorVSDamage(df):
    getConditionalProbabilitiesOperatorVSDamage(df)

def getTop10ManufacturersVSDamage(df):
    getConditionalProbabilitiesTop10ManufacturersVSDamage(df)

def getTop10ManufacturersVSInjuries(df):
    getConditionalProbabilitiesTop10ManufacturersVSInjuries(df)

def getTop10CommercialOrganizationsVSDamage(df):
    getConditionalProbabilitiesTop10CommercialOrganizationsVSDamage(df)