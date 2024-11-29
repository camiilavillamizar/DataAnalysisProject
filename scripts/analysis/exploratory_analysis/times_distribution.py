from datetime import datetime
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, gamma, weibull_min, uniform

def plotDistributions(df):
    df['TimeInSeconds'] = df['OccTime'].apply(time_to_seconds)
    df_time_filtered = df[df['TimeInSeconds'].notna()].copy()

    #Creating a continuous range for the seconds of the day
    x_range = np.linspace(df_time_filtered['TimeInSeconds'].min(), df_time_filtered['TimeInSeconds'].max(), 1000)

    #Statistics for distribution calculations
    a = df_time_filtered['TimeInSeconds'].min()  # Minimum time in seconds
    b = df_time_filtered['TimeInSeconds'].max()  # Maximum time in seconds
    mean_time = df_time_filtered['TimeInSeconds'].mean()  # Mean time
    std_time = df_time_filtered['TimeInSeconds'].std()  # Standard deviation of time

    #distributions
    distributions = {
        "Uniform": uniform.pdf(x_range, loc=a, scale=b - a),
        "Normal": norm.pdf(x_range, loc=mean_time, scale=std_time),
        "Exponential": expon.pdf(x_range, loc=df_time_filtered['TimeInSeconds'].min(), scale=df_time_filtered['TimeInSeconds'].mean()),
        "Gamma": gamma.pdf(x_range, a=2, loc=df_time_filtered['TimeInSeconds'].min(), scale=std_time),
        "Weibull": weibull_min.pdf(x_range, c=1.5, loc=df_time_filtered['TimeInSeconds'].min(), scale=std_time),
    }

    #MSE for each distribution
    mse_results = {}
    for name, pdf in distributions.items():
        hist, bin_edges = np.histogram(df_time_filtered['TimeInSeconds'], bins=30, density=True)
        bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])  # Calculate the bin centers
        mse_results[name] = mean_squared_error(hist, np.interp(bin_centers, x_range, pdf))  # Interpolate PDFs to bin centers

    #esults
    best_fit = min(mse_results, key=mse_results.get)
    print("Best fitting distribution:", best_fit)
    print("Mean Squared Errors (MSE) for distributions:")
    for name, mse in mse_results.items():
        print(f"{name}: {mse:.6f}")

    #Functions to convert seconds into hours and minutes format (HH:MM)
    def seconds_to_hours(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{int(hours):02}:{int(minutes):02}"  # Format as HH:MM

    #Creating custom labels for the X-axis (time labels)
    x_ticks = np.linspace(df_time_filtered['TimeInSeconds'].min(), df_time_filtered['TimeInSeconds'].max(), 12)  # Increase number of labels
    x_labels = [seconds_to_hours(tick) for tick in x_ticks]

    #Plotting the histogram and PDFs
    plt.figure(figsize=(14, 8))  # Make the plot wider for better readability
    plt.hist(df_time_filtered['TimeInSeconds'], bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Real Data')
    for name, pdf in distributions.items():
        plt.plot(x_range, pdf, label=f"{name} Distribution")
    plt.title(f'Distribution of Incident Times (Best Fit: {best_fit})')
    plt.xlabel('Time (hours)')
    plt.ylabel('Density')
    plt.xticks(ticks=x_ticks, labels=x_labels)  # Apply custom time labels
    plt.legend()
    plt.show()

#function to convert OccTime to seconds of the day
def time_to_seconds(time_str):
    try:
        time_obj = datetime.strptime(time_str, '%H:%M:%S')
        return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    except ValueError:
        return np.nan

