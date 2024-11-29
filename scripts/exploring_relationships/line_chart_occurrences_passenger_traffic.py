
import matplotlib.pyplot as plt

def plotLineChartOccurrencesAndPassengerTraffic(df):
    # Filter the DataFrame to keep only rows where both 'occurrences' and 'passenger_traffic' have values
    df_cleaned = df[['YearMonth', 'occurrences_normalized', 'passenger_traffic_normalized']].dropna()

    # Add a 'Quarter' column to group data by year and quarter
    df_cleaned['Quarter'] = df_cleaned['YearMonth'].dt.to_period('Q')

    # Group by quarter and calculate the mean for each quarter
    quarterly_data = df_cleaned.groupby('Quarter')[['occurrences_normalized', 'passenger_traffic_normalized']].mean()

    # Reset the index to prepare for plotting
    quarterly_data.reset_index(inplace=True)

    # Convert 'Quarter' back to a timestamp for plotting
    quarterly_data['Quarter'] = quarterly_data['Quarter'].dt.to_timestamp()

    # Plotting occurrences and passenger traffic over quarters
    plt.figure(figsize=(14, 7))
    plt.plot(quarterly_data['Quarter'], quarterly_data['occurrences_normalized'], label='Occurrences', marker='o', alpha=0.8)
    plt.plot(quarterly_data['Quarter'], quarterly_data['passenger_traffic_normalized'], label='Passenger Traffic', marker='o', alpha=0.8)

    # Customize the chart
    plt.title('Occurrences and Passenger Traffic by Quarter')
    plt.xlabel('Year-Quarter')
    plt.ylabel('Average Normalized Value')

    # Customize grid
    plt.grid(axis='both', linestyle='--', linewidth=0.7, alpha=0.6, color='gray')  # Enhancing grid appearance

    # Set X-axis ticks to display quarters
    plt.xticks(quarterly_data['Quarter'], labels=[f"Q{q.quarter}-{q.year}" for q in quarterly_data['Quarter']], rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.show()
