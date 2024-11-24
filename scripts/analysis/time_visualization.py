import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pandas as pd
import numpy as np
import calendar


def visualize_incident_times(df, figsize=(15, 8)):
    """
    Create visualizations showing the distribution of incidents across different times of the day.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing the 'OccTime' column in 'HH:MM:SS' format
    figsize : tuple, optional
        Figure size as (width, height)
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    
    # Convert time strings to datetime.time objects and extract hour
    df['Hour'] = df['OccTime'].apply(lambda x: datetime.strptime(x, '%H:%M:%S').hour)
    
    # Calculate frequencies
    hourly_counts = df['Hour'].value_counts().sort_index()
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize, height_ratios=[2, 1])
    
    # Plot 1: Line plot with markers
    ax1.plot(hourly_counts.index, hourly_counts.values, marker='o', linewidth=2, markersize=8)
    ax1.set_title('Incident Frequency by Hour of Day', pad=20)
    ax1.set_xlabel('Hour (24-hour format)')
    ax1.set_ylabel('Number of Incidents')
    ax1.grid(True, alpha=0.3)
    
    # Customize x-axis
    ax1.set_xticks(range(24))
    ax1.set_xticklabels([f'{i:02d}:00' for i in range(24)])
    
    # Add value labels on the points
    for x, y in zip(hourly_counts.index, hourly_counts.values):
        ax1.annotate(str(y), (x, y), textcoords="offset points", xytext=(0,10), ha='center')
    
    # Plot 2: Heatmap showing hourly distribution
    hourly_matrix = hourly_counts.values.reshape(1, -1)
    sns.heatmap(hourly_matrix, 
                ax=ax2, 
                cmap='YlOrRd',
                cbar_kws={'label': 'Number of Incidents'},
                xticklabels=[f'{i:02d}:00' for i in range(24)],
                yticklabels=[''])
    ax2.set_title('Heatmap of Incident Frequency')
    
    # Rotate x-axis labels for better readability
    plt.setp(ax1.get_xticklabels(), rotation=45)
    plt.setp(ax2.get_xticklabels(), rotation=45)
    
    # Adjust layout
    plt.tight_layout()

def get_time_statistics(df):
    """
    Calculate and return various statistics about incident timing.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing the 'OccTime' column in 'HH:MM:SS' format
    
    Returns:
    --------
    dict
        Dictionary containing various time-related statistics
    """
    # Convert time strings to datetime.time objects and extract hour
    df['Hour'] = df['OccTime'].apply(lambda x: datetime.strptime(x, '%H:%M:%S').hour)
    
    # Calculate statistics
    hourly_counts = df['Hour'].value_counts().sort_index()
    
    stats = {
        'peak_hour': f"{hourly_counts.idxmax():02d}:00",
        'peak_hour_incidents': hourly_counts.max(),
        'quietest_hour': f"{hourly_counts.idxmin():02d}:00",
        'quietest_hour_incidents': hourly_counts.min(),
        'morning_incidents': hourly_counts[6:12].sum(),  # 6 AM to 11:59 AM
        'afternoon_incidents': hourly_counts[12:18].sum(),  # 12 PM to 5:59 PM
        'evening_incidents': hourly_counts[18:24].sum(),  # 6 PM to 11:59 PM
        'night_incidents': hourly_counts[0:6].sum(),  # 12 AM to 5:59 AM
    }
    
    return stats

def create_province_year_heatmap(df, figsize=(15, 8)):
    """
    Create a heatmap showing the number of occurrences by province and year for Canadian data.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing:
        - OccDate: Date of occurrence
        - CountryID_DisplayEng: Country name
        - ProvinceID_DisplayEng: Province name
    figsize : tuple, optional
        Figure size as (width, height)
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    # Filter for Canadian data
    canada_data = df[
        (df['CountryID_DisplayEng'] == 'CANADA') & 
        (df['ProvinceID_DisplayEng'].notna())
    ].copy()
    
    # Convert date and extract year
    canada_data['Year'] = pd.to_datetime(canada_data['OccDate']).dt.year
    
    # Create pivot table for heatmap
    pivot_data = canada_data.pivot_table(
        values='OccDate',
        index='ProvinceID_DisplayEng',
        columns='Year',
        aggfunc='count',
        fill_value=0
    )
    
    # Calculate percentage change year over year
    pct_change = pivot_data.pct_change(axis=1) * 100
    
    # Replace infinite values with NaN
    pct_change = pct_change.replace([np.inf, -np.inf], np.nan)
    
    # For cells where previous value was 0, calculate percentage based on current value
    # for col in pct_change.columns:
    #     mask = pivot_data[col].shift(1) == 0
    #     if mask.any():
    #         pct_change.loc[mask, col] = np.nan
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create heatmap
    sns.heatmap(pct_change,
                cmap='RdYlBu',      # Red for negative, Blue for positive
                center=0,           # Center the colormap at 0
                fmt='.0f',          # Format as integer percentage
                cbar_kws={'label': 'Year-over-Year Change (%)',
                         'orientation': 'horizontal'},
                ax=ax,
                mask=pct_change.isna(),  # Mask NaN values
                vmin=-20,           # Set minimum value for color scale
                vmax=20)            # Set maximum value for color scale
    
    # Customize the plot
    ax.set_title('Year-over-Year Change in Incidents by Province (%)', 
                pad=20, fontsize=14)
    ax.set_ylabel('')
    
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()

def create_province_month_heatmap(df, figsize=(15, 8)):
    """
    Create a heatmap showing the number of occurrences by province and month for Canadian data.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing:
        - OccDate: Date of occurrence
        - CountryID_DisplayEng: Country name
        - ProvinceID_DisplayEng: Province name
    figsize : tuple, optional
        Figure size as (width, height)
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    # Define valid provinces
    valid_provinces = [
        'ONTARIO',
        'QUEBEC',
        'BRITISH COLUMBIA',
        'ALBERTA',
        'MANITOBA',
        'SASKATCHEWAN',
        'NOVA SCOTIA',
        'NEW BRUNSWICK',
        'NEWFOUNDLAND AND LABRADOR',
        'PRINCE EDWARD ISLAND',
        'NORTHWEST TERRITORIES',
        'YUKON',
        'NUNAVUT'
    ]
    
    # Filter for Canadian data
    canada_data = df[
        (df['CountryID_DisplayEng'] == 'CANADA') & 
        (df['ProvinceID_DisplayEng'].isin(valid_provinces))
    ].copy()
    
    # Convert date and extract month
    canada_data['Date'] = pd.to_datetime(canada_data['OccDate'])
    canada_data['Month'] = canada_data['Date'].dt.month
    
    # Create pivot table for monthly occurrences
    pivot_data = canada_data.pivot_table(
        values='OccDate',
        index='ProvinceID_DisplayEng',
        columns='Month',
        aggfunc='count',
        fill_value=0
    )
    
    # Rename columns to month names
    pivot_data.columns = [calendar.month_abbr[m] for m in pivot_data.columns]
    
    # Calculate percentage of annual total for each province
    row_totals = pivot_data.sum(axis=1)
    percentage_data = pivot_data.div(row_totals, axis=0) * 100
    
    # Create figure and axis
    _, ax = plt.subplots(figsize=figsize)
    
    # Create heatmap
    sns.heatmap(percentage_data,
                cmap='YlOrRd',      # Yellow to Orange to Red colormap
                fmt='.1f',          # Format as float with 1 decimal
                cbar_kws={'label': '% of Annual Incidents',
                         'orientation': 'horizontal'},
                ax=ax)
    
    # Customize the plot
    ax.set_title('Monthly Distribution of Incidents by Province\n(% of Annual Total)', 
                pad=20, fontsize=14)
    ax.set_ylabel('')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)

    ax.tick_params(axis='y', pad=5) 
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()