import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from collections import Counter
import numpy as np

def plot_coordinates_matplotlib(coordinates_list):
    """
    Plot coordinates on a complete world map using matplotlib and cartopy.
    
    Parameters:
    coordinates_list: List of tuples containing (latitude, longitude)
    """
    # Create figure and axis with projection
    plt.figure(figsize=(20, 10))
    ax = plt.axes(projection=ccrs.Robinson())  # Using Robinson projection for better world view
    
    # Set map bounds to show entire world
    ax.set_global()
    
    # Add map features
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)
    
    # Plot each coordinate
    for lat, lon in coordinates_list:
        plt.plot(lon, lat, 'ro', markersize=8, transform=ccrs.PlateCarree())
    
    # Add gridlines
    ax.gridlines(linewidth=0.5, linestyle='--', color='gray')
    
    # Set title
    plt.title('World Map with Incidents', pad=20)
    
    # Show the plot
    plt.show()

def plot_frequency(data_list, title="Frequency Distribution", figsize=(10, 6), 
                  color='skyblue', edgecolor='navy', ylabel="Frequency", 
                  xlabel="Values", rotation=45):
    """
    Creates a column chart showing the frequency of unique values in a list.
    
    Parameters:
    -----------
    data_list : list
        Input list containing the values to analyze
    title : str, optional
        Title of the plot (default: "Frequency Distribution")
    figsize : tuple, optional
        Size of the figure (width, height) in inches (default: (10,6))
    color : str, optional
        Color of the bars (default: 'skyblue')
    edgecolor : str, optional
        Color of the bar edges (default: 'navy')
    ylabel : str, optional
        Label for y-axis (default: "Frequency")
    xlabel : str, optional
        Label for x-axis (default: "Values")
    rotation : int, optional
        Rotation angle for x-axis labels (default: 45)
    
    Returns:
    --------
    None : Displays the plot
    """
    
    # Count frequencies using Counter
    counter = Counter(data_list)
    
    # Sort the counter items by value for better visualization
    sorted_items = sorted(counter.items())
    values, frequencies = zip(*sorted_items)
    
    # Create the plot
    plt.figure(figsize=figsize)
    
    # Create bars with a bit of space between them
    x = np.arange(len(values))
    plt.bar(x, frequencies, color=color, edgecolor=edgecolor, width=0.7)
    
    # Customize the plot
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Set x-axis ticks and labels
    plt.xticks(x, values, rotation=rotation)
    
    # Add value labels on top of each bar
    for i, freq in enumerate(frequencies):
        plt.text(i, freq, str(freq), ha='center', va='bottom')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Show the plot
    plt.show()