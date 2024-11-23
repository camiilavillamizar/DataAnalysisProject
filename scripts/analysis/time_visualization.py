import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


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