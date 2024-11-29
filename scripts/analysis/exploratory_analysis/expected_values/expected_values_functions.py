from analysis.exploratory_analysis.expected_values.damage_by_weight import plotDamageByWeight
from analysis.exploratory_analysis.expected_values.aircraft_age_by_operation import plotAircraftAgeByOperation
from analysis.exploratory_analysis.expected_values.injuries_by_aircraft import plotInjuriesByAircraft
from analysis.exploratory_analysis.expected_values.damage_by_operator import plotDamageByOperator
from analysis.exploratory_analysis.expected_values.damage_by_province import plotDamageByProvince

def getDamageByWeight(df):
    plotDamageByWeight(df)

def getAircraftAgeByOperation(df):
    plotAircraftAgeByOperation(df)

def getInjuriesByAircraft(df):
    plotInjuriesByAircraft(df)

def getDamageByOperator(df):
    plotDamageByOperator(df)

def gettDamageByProvince(df):
    plotDamageByProvince(df)