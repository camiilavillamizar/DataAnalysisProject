import numpy as np
from scipy.stats import binom
from scipy.special import gammaln
import matplotlib.pyplot as plt

def getBinomialProbabilityForInjuries(df):
    #Probability of injuries
    p_injuries = (df['InjuriesEnum_DisplayEng'] == 'Yes').mean()
    #Total of accidents/incidents
    n_occurrences = len(df)
    #Total of injuries
    n_injuries = (df['InjuriesEnum_DisplayEng'] == 'Yes').sum()

    n_occurrences_sample = 10

    printValues(p_injuries, n_occurrences, n_injuries, n_occurrences_sample)
    plotResult(n_occurrences_sample, p_injuries)

def printValues(p_injuries, n_occurrences, n_injuries, n_occurrences_sample):
    print(f"Number of injuries: {n_injuries}")
    print(f"Injuries probability: {p_injuries}")
    print(f"Total number of occurrences: {n_occurrences}")

    for x in range(0, n_occurrences_sample + 1):
        prob = binomial_log_pmf(x, n_occurrences_sample, p_injuries)
        print(f"Probability of {x} injuries in {n_occurrences_sample} occurrences: {prob:.10}")

def binomial_log_pmf(x, n, p):
    log_prob = (
        gammaln(n + 1) - gammaln(x + 1) - gammaln(n - x + 1) 
        + x * np.log(p)  # Log(p^x)
        + (n - x) * np.log(1 - p)  # Log((1-p)^(n-x))
    )
    return np.exp(log_prob) 

def plotResult(n_occurrences,  p_injuries ):
    x_values = list(range(0, n_occurrences + 1))
    probabilities = [binomial_log_pmf(x, n_occurrences, p_injuries) for x in x_values]

    plt.figure(figsize=(10, 6))
    plt.bar(x_values, probabilities, color='#80549c', edgecolor='black')
    plt.title('Binomial Distribution: Probability of Injuries in 10 Occurrences')
    plt.xlabel('Number of Injuries')
    plt.ylabel('Probability')
    plt.xticks(x_values)  
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()