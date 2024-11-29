import matplotlib.pyplot as plt
import pandas as pd

def plotLineChart(df):

    df['YearMonth'] = pd.to_datetime(df['YearMonth'])


    # Extract the month for grouping
    df['Month'] = df['YearMonth'].dt.month

    # Normalize all relevant columns
    df['occurrences_normalized'] = (df['occurrences'] - df['occurrences'].mean()) / df['occurrences'].std()
    df['births_normalized'] = (df['births'] - df['births'].mean()) / df['births'].std()
    df['dollar_exchange_normalized'] = (df['dollar_exchange'] - df['dollar_exchange'].mean()) / df['dollar_exchange'].std()
    df['passenger_traffic_normalized'] = (df['passenger_traffic'] - df['passenger_traffic'].mean()) / df['passenger_traffic'].std()

    # Group by month to find seasonal patterns
    monthly_data = df.groupby('Month')[['occurrences_normalized', 'births_normalized', 'dollar_exchange_normalized', 'passenger_traffic_normalized']].mean()

    # Plot seasonal trends as a line chart
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data.index, monthly_data['occurrences_normalized'], label='Occurrences (Normalized)', marker='o')
    plt.plot(monthly_data.index, monthly_data['births_normalized'], label='Births (Normalized)', marker='o')
    #plt.plot(monthly_data.index, monthly_data['dollar_exchange_normalized'], label='Dollar Exchange (Normalized)', marker='o')
    plt.plot(monthly_data.index, monthly_data['passenger_traffic_normalized'], label='Passenger Traffic (Normalized)', marker='o')

    # Customize the chart
    plt.title('Seasonal Trends in Normalized Occurrences, Births and Passenger Traffic')
    plt.xlabel('Month')
    plt.ylabel('Average Normalized Value')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()