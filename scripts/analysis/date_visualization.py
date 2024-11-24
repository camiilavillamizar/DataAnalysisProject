import pandas as pd
import matplotlib.pyplot as plt
import calendar
import numpy as np


def visualize_date_frequencies(df, figsize=(15, 12)):
    """
    Create visualizations showing the distribution of incidents across different date components
    (monthly, daily, and day of month) in a 2-row layout.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing the 'OccDate' column in 'YYYY-MM-DD' format
    figsize : tuple, optional
        Figure size as (width, height)
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    # Convert date strings to datetime
    df['Date'] = pd.to_datetime(df['OccDate'])
    
    # Extract components
    df['Month'] = df['Date'].dt.month
    df['DayOfWeek'] = df['Date'].dt.day_name()
    df['DayOfMonth'] = df['Date'].dt.day
    
    # Create figure with subplots in 2 rows
    fig = plt.figure(figsize=figsize)
    
    # Define grid for subplots
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1])
    
    # Create axes
    ax1 = fig.add_subplot(gs[0, 0])  # First row, first column
    ax2 = fig.add_subplot(gs[0, 1])  # First row, second column
    ax3 = fig.add_subplot(gs[1, :])  # Second row, span both columns
    
    # 1. Monthly Distribution
    monthly_counts = df['Month'].value_counts().sort_index()
    month_names = [calendar.month_name[i] for i in monthly_counts.index]
    
    # Set x-ticks properly for months
    x_positions = np.arange(len(month_names))
    ax1.bar(x_positions, monthly_counts.values)
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(month_names, rotation=45, ha='right')
    ax1.set_title('Incidents by Month')
    ax1.set_ylabel('Number of Incidents')
    
    # Add value labels on the bars
    for i, v in enumerate(monthly_counts.values):
        ax1.text(i, v, str(v), ha='center', va='bottom')
    
    # 2. Day of Week Distribution
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_counts = df['DayOfWeek'].value_counts()
    daily_counts = daily_counts.reindex(day_order)
    
    # Set x-ticks properly for days
    x_positions = np.arange(len(day_order))
    ax2.bar(x_positions, daily_counts.values)
    ax2.set_xticks(x_positions)
    ax2.set_xticklabels(day_order, rotation=45, ha='right')
    ax2.set_title('Incidents by Day of Week')
    ax2.set_ylabel('Number of Incidents')
    
    # Add value labels on the bars
    for i, v in enumerate(daily_counts.values):
        ax2.text(i, v, str(v), ha='center', va='bottom')
    
    # 3. Day of Month Distribution
    daily_month_counts = df['DayOfMonth'].value_counts().sort_index()
    
    ax3.bar(daily_month_counts.index, daily_month_counts.values)
    ax3.set_title('Incidents by Day of Month')
    ax3.set_xlabel('Day of Month')
    ax3.set_ylabel('Number of Incidents')
    
    # Add value labels on the bars
    for i, v in zip(daily_month_counts.index, daily_month_counts.values):
        ax3.text(i, v, str(v), ha='center', va='bottom', fontsize=8)
    
    # Adjust layout with more control
    plt.tight_layout()



def visualize_yearly_trend(df, figsize=(12, 6), min_frequency=10):
    """
    Create a visualization showing the yearly trend of incidents,
    excluding years with frequencies below the minimum threshold.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing the 'OccDate' column in 'YYYY-MM-DD' format
    figsize : tuple, optional
        Figure size as (width, height)
    min_frequency : int, optional
        Minimum number of incidents required to include a year in the visualization
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    # Convert date strings to datetime and extract year
    df['Date'] = pd.to_datetime(df['OccDate'])
    df['Year'] = df['Date'].dt.year
    
    # Calculate yearly counts and filter
    yearly_counts = df['Year'].value_counts().sort_index()
    yearly_counts = yearly_counts[yearly_counts >= min_frequency]
    
    if len(yearly_counts) == 0:
        raise ValueError(f"No years have {min_frequency} or more incidents")
    
    # Create figure
    _, ax = plt.subplots(figsize=figsize)
    
    # Plot yearly trend
    ax.plot(yearly_counts.index, yearly_counts.values, 
            marker='o', linewidth=2, markersize=8, color='#80549c')
    ax.set_title('Yearly Trend of Incidents', pad=20, fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Number of Incidents', fontsize=12)
    
    # Customize grid
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis to start at 0
    ax.set_ylim(bottom=0)
    
    # Add light gray background grid
    ax.grid(True, linestyle='--', alpha=0.3, color='gray')
    ax.set_axisbelow(True)  # Ensure grid is behind the data points
    
    plt.tight_layout()


def visualize_quarterly_trend(df, figsize=(15, 7), min_frequency=10):
    """
    Create a visualization showing the quarterly trend of incidents with color-coded quarters.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing the 'OccDate' column in 'YYYY-MM-DD' format
    figsize : tuple, optional
        Figure size as (width, height)
    min_frequency : int, optional
        Minimum number of incidents required to include a quarter
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    # Convert date strings to datetime
    df['Date'] = pd.to_datetime(df['OccDate'])
    
    # Create quarter information
    df['Year'] = df['Date'].dt.year
    df['Quarter'] = df['Date'].dt.quarter
    df['YearQuarter'] = df['Year'].astype(str) + '-Q' + df['Quarter'].astype(str)
    
    # Calculate quarterly counts and filter
    quarterly_counts = df.groupby(['Year', 'Quarter']).size().reset_index(name='Count')
    quarterly_counts = quarterly_counts[quarterly_counts['Count'] >= min_frequency]
    
    if len(quarterly_counts) == 0:
        raise ValueError(f"No quarters have {min_frequency} or more incidents")
    
    # Create x-axis positions
    quarterly_counts['x_position'] = quarterly_counts['Year'] + (quarterly_counts['Quarter']-1)/4
    
    # Create figure
    _, ax = plt.subplots(figsize=figsize)
    
    # Define colors for quarters
    quarter_colors = {
        1: '#1f77b4',  # Blue
        2: '#2ca02c',  # Green
        3: '#ff7f0e',  # Orange
        4: '#d62728'   # Red
    }
    
    # Plot points for each quarter with different colors
    for quarter, color in quarter_colors.items():
        mask = quarterly_counts['Quarter'] == quarter
        quarter_data = quarterly_counts[mask]
        ax.plot(quarter_data['x_position'], quarter_data['Count'], 
                marker='o', linestyle='-', markersize=6, color=color,
                label=f'Q{quarter}', alpha=0.7)
    
    # Customize the plot
    ax.set_title('Quarterly Trend of Incidents', pad=20, fontsize=14)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Number of Incidents', fontsize=12)
    
    # Set x-axis ticks (show every 5 years)
    all_years = quarterly_counts['Year'].unique()
    tick_years = np.arange(all_years.min() - (all_years.min() % 5), 
                          all_years.max() + 5, 5)
    ax.set_xticks(tick_years)
    ax.set_xticklabels(tick_years.astype(int), rotation=0)
    
    # Add light grid
    ax.grid(True, linestyle='--', alpha=0.3, color='gray')
    ax.set_axisbelow(True)
    
    # Set y-axis to start at 0
    ax.set_ylim(bottom=0)
    
    # Add legend
    ax.legend(title='Quarter', bbox_to_anchor=(1.02, 1), loc='upper left')
    
    # Add minor gridlines for years
    ax.set_xticks(all_years, minor=True)
    ax.grid(True, which='minor', linestyle=':', alpha=0.2)
    
    # Adjust layout to make room for legend
    plt.subplots_adjust(right=0.95)