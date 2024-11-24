import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from scipy.stats import gaussian_kde
import pandas as pd
import geopandas as gpd
import numpy as np
import json
from urllib.request import urlopen

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


def create_canada_frequency_choropleth(data_df, figsize=(15, 10)):
    """
    Create a choropleth map of Canadian provinces showing frequency of occurrences.
    Handles uppercase province names in the input data.
    
    Parameters:
    -----------
    data_df : pandas DataFrame
        Input DataFrame containing:
        - ProvinceID_DisplayEng: Province names in English (in uppercase)
        - Latitude: Latitude values
        - Longitude: Longitude values
    figsize : tuple, optional
        Figure size as (width, height)
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    
    # Filter for Canadian coordinates
    canada_data = data_df[
        (data_df['Latitude'] > 0) & 
        (data_df['Longitude'] < 0)
    ].copy()

    # Create a mapping dictionary for uppercase province names
    province_name_mapping = {
        'ONTARIO': 'Ontario',
        'QUEBEC': 'Quebec',
        'BRITISH COLUMBIA': 'British Columbia',
        'ALBERTA': 'Alberta',
        'MANITOBA': 'Manitoba',
        'SASKATCHEWAN': 'Saskatchewan',
        'NOVA SCOTIA': 'Nova Scotia',
        'NEW BRUNSWICK': 'New Brunswick',
        'NEWFOUNDLAND AND LABRADOR': 'Newfoundland and Labrador',
        'PRINCE EDWARD ISLAND': 'Prince Edward Island',
        'NORTHWEST TERRITORIES': 'Northwest Territories',
        'YUKON': 'Yukon Territory',
        'NUNAVUT': 'Nunavut'
    }
    
    # Map the province names to proper case
    canada_data['ProvinceID_DisplayEng'] = canada_data['ProvinceID_DisplayEng'].map(province_name_mapping)
    
    # Calculate frequency of each province
    province_frequencies = canada_data['ProvinceID_DisplayEng'].value_counts().reset_index()
    province_frequencies.columns = ['ProvinceID_DisplayEng', 'Frequency']
    
    # Load Canada provinces GeoJSON
    provinces_url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/canada.geojson"
    with urlopen(provinces_url) as response:
        provinces_json = json.load(response)
    
    # Create GeoDataFrame from GeoJSON
    provinces = gpd.GeoDataFrame.from_features(provinces_json["features"])
    
    # Merge frequency data with geographic information
    provinces = provinces.merge(
        province_frequencies,
        left_on='name',
        right_on='ProvinceID_DisplayEng',
        how='left'
    )
    
    # Create the figure and axis
    _, ax = plt.subplots(1, 1, figsize=figsize)
    
    # Plot the choropleth
    provinces.plot(
        column='Frequency',
        ax=ax,
        legend=True,
        legend_kwds={
            'label': 'Frequency',
            'orientation': 'vertical'
        },
        missing_kwds={
            'color': 'lightgrey'
        },
        cmap='Blues',
        edgecolor="Black",
        linewidth=0.1
    )
    
    # Customize the map
    ax.axis('off')
    ax.set_title('Frequency by Province', pad=20, fontsize=16)
    
    # Add province labels with frequencies
    # for _, row in provinces.iterrows():
    #     freq = row['Frequency']
    #     label = f"{row['name']}\n({int(freq) if pd.notnull(freq) else 0})"
    #     ax.annotate(
    #         text=label,
    #         xy=(row.geometry.centroid.x, row.geometry.centroid.y),
    #         horizontalalignment='center',
    #         fontsize=8
    #     )
    
    plt.tight_layout()