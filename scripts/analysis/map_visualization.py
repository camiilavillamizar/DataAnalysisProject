import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from collections import Counter
import numpy as np
from scipy.stats import gaussian_kde

def plot_coordinates_heatmap(coordinates_list):
    """
    Plot coordinates as a heatmap on a complete world map using matplotlib and cartopy.
    
    Parameters:
    coordinates_list: List of tuples containing (latitude, longitude)
    """
    
    # Input validation
    if not coordinates_list:
        raise ValueError("coordinates_list is empty")
    
    # Create figure and axis with projection
    plt.figure(figsize=(20, 10))
    ax = plt.axes(projection=ccrs.Robinson())
    
    # Set map bounds to show entire world
    ax.set_global()
    
    # Add map features
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)
    
    try:
        # Separate latitude and longitude
        lats, lons = zip(*coordinates_list)
        
        # Create a grid of points with higher resolution
        lon_grid, lat_grid = np.mgrid[-180:181:361j, -90:91:181j]
        
        # Stack coordinates into a 2D array
        positions = np.vstack([lons, lats])
        
        # Create kernel density estimate with smaller bandwidth
        # The smaller the bandwidth, the more sensitive the heatmap
        kernel = gaussian_kde(positions, bw_method='scott')  # Start with scott method
        kernel.set_bandwidth(kernel.factor / 5)  # Reduce bandwidth to increase sensitivity
        
        # Calculate density on the grid
        grid_coords = np.vstack([lon_grid.ravel(), lat_grid.ravel()])
        z = kernel(grid_coords)
        
        # Reshape back to grid
        z = z.reshape(lon_grid.shape)
        
        # Apply non-linear scaling to enhance visibility of lower density areas
        z = np.power(z, 0.1)  # Adjust this value to change sensitivity
        
        # Plot heatmap
        img = ax.pcolormesh(lon_grid, lat_grid, z,
                           transform=ccrs.PlateCarree(),
                           cmap='YlOrRd',
                           shading='auto',
                           alpha=0.7)
        
        # Add colorbar with scientific notation
        cbar = plt.colorbar(img, ax=ax, orientation='horizontal',
                           label='Incident Density (normalized)',
                           pad=0.05,
                           format='%.2e')
        cbar.ax.tick_params(labelsize=10)
        
    except Exception as e:
        print(f"Error creating heatmap: {e}")
        print("Falling back to scatter plot...")
        try:
            scatter = ax.scatter(lons, lats, c='red', s=20, alpha=0.5,
                               transform=ccrs.PlateCarree())
            plt.colorbar(scatter, orientation='horizontal',
                        label='Incident Location',
                        pad=0.05)
        except Exception as e:
            print(f"Could not create scatter plot either: {e}")
            return
    
    # Add gridlines
    ax.gridlines(linewidth=0.5, linestyle='--', color='gray')
    
    # Set title
    plt.title('World Map Incident Density Heatmap', pad=20, size=14)
    
    # Show the plot
    plt.tight_layout()
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