import pandas as pd
import numpy as np
from scipy.stats import norm, expon, gamma, lognorm, beta, weibull_min
import matplotlib.pyplot as plt



def plotingDistributions(df): 
    plottingNormalDistribution(df)
    results = findingBestDistribution(df)
    results_df = pd.DataFrame(results)
    return results_df

def plottingNormalDistribution(df):
    #Calculating age of aircrafts
    df['AircraftAge'] = pd.to_datetime(df['OccDate']).dt.year - df['YearOfManuf']
    df_filtered = df[df['AircraftAge'] > 0]

    #Fitting a normal distribution
    mean_age = df_filtered['AircraftAge'].mean()
    std_age = df_filtered['AircraftAge'].std()

    x = np.linspace(df_filtered['AircraftAge'].min(), df_filtered['AircraftAge'].max(), 1000)
    pdf = norm.pdf(x, mean_age, std_age)

    #Graph
    plt.figure(figsize=(10, 6))
    plt.hist(df_filtered['AircraftAge'], bins=30, density=True, alpha=0.6, color='#80549c', edgecolor='black', label='Real data')
    plt.plot(x, pdf, 'r-', label='Normal distribution fitted')
    plt.title('Normal distribution for aircrafts age')
    plt.xlabel('Years')
    plt.ylabel('Density')
    plt.legend()
    plt.show()


def findingBestDistribution(df):
    aircraft_ages = df['AircraftAge'] 

    #Setting a range
    x = np.linspace(aircraft_ages.min(), aircraft_ages.max(), 1000)

    #Dict to store results
    results = {}  

    #Fitting each distribution
    fit_and_plot_distribution(expon, "Exponential Distribution", aircraft_ages, results, x)
    fit_and_plot_distribution(gamma, "Gamma Distribution", aircraft_ages, results, x)
    fit_and_plot_distribution(lognorm, "Log-Normal Distribution", aircraft_ages, results, x)
    fit_and_plot_distribution(beta, "Beta Distribution", aircraft_ages, results, x)
    fit_and_plot_distribution(weibull_min, "Weibull Distribution", aircraft_ages, results, x)

    #Compraring results
    best_fit = min(results, key=lambda k: results[k]['mse'])
    print("Best fit:", best_fit)
    print("Params:", results[best_fit]['params'])

    return results

def fit_and_plot_distribution(dist, dist_name, aircraft_ages, results, x):

    params = dist.fit(aircraft_ages)
    fitted_pdf = dist.pdf(x, *params)

    histogram_values, bin_edges = np.histogram(aircraft_ages, bins=30, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    mse = np.mean((dist.pdf(bin_centers, *params) - histogram_values)**2)
    
    results[dist_name] = {'params': params, 'mse': mse}

    plt.figure(figsize=(10, 6))
    plt.hist(aircraft_ages, bins=30, density=True, alpha=0.6, color='#80549c', edgecolor='black', label='Real Data')
    plt.plot(x, fitted_pdf, 'r-', label=f'{dist_name} Fitted (MSE={mse:.4f})')
    plt.title(f'{dist_name} Fitted to the aircreaft Ages')
    plt.xlabel('Age')
    plt.ylabel('Density')
    plt.legend()
    plt.show()