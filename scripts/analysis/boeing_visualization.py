import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def analyze_boeing_occurrences(df):
    """
    Analyzes and plots Boeing aircraft occurrences against stock price trends
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing OccDate and AircraftMakeID_DisplayEng columns
    
    Returns:
    None (displays plot)
    """
    # Convert OccDate to datetime if not already
    df['OccDate'] = pd.to_datetime(df['OccDate'])
    
    # Filter for Boeing aircraft and group by year
    boeing_df = df[df['AircraftMakeID_DisplayEng'].str.contains('BOEING', na=False)].copy()
    yearly_occurrences = boeing_df.groupby(boeing_df['OccDate'].dt.year).size().reset_index()
    yearly_occurrences.columns = ['Year', 'Occurrences']
    
    # Get Boeing stock data
    # Get the date range from the occurrence data
    start_year = yearly_occurrences['Year'].min()
    end_year = yearly_occurrences['Year'].max()
    
    # Fetch Boeing stock data with daily interval
    boeing_stock = yf.download('BA', 
                             start=f'{start_year}-01-01',
                             end=f'{end_year + 1}-01-01',
                             interval='1d')
    
    # Calculate yearly average stock price
    boeing_stock.index = pd.to_datetime(boeing_stock.index)
    yearly_stock = boeing_stock.groupby(boeing_stock.index.year)['Adj Close'].mean().reset_index()
    yearly_stock.columns = ['Year', 'Stock_Price']
    
    # Create the plot
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Plot occurrences
    color = 'tab:blue'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Occurrences', color=color)
    line1 = ax1.plot(yearly_occurrences['Year'], yearly_occurrences['Occurrences'], 
                     color=color, label='Occurrences', marker='o')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Create second y-axis for stock price
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Stock Price (USD)', color=color)
    line2 = ax2.plot(yearly_stock['Year'], yearly_stock['Stock_Price'], 
                     color=color, label='Stock Price', marker='o')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Add title and legend
    plt.title('Boeing Aircraft Occurrences vs Stock Price Over Time')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()