import matplotlib.pyplot as plt
import numpy as np

def plot_manufacturing_year_histogram(year_data, title="Distribution of Manufacturing Years", 
                                    figsize=(12, 6), color='purple', 
                                    edgecolor='black', bins=None):
    plt.figure(figsize=figsize)
    
    # Calculate optimal bins if not specified
    if bins is None:
        bins = int(np.log2(len(year_data)) + 1)
    
    # Create histogram and get the bins edges
    n, bins_edges, patches = plt.hist(year_data, bins=bins, color=color, edgecolor=edgecolor)
    
    # Add year labels under each bar
    bin_centers = bins_edges[:-1] + np.diff(bins_edges) / 2
    plt.xticks(bin_centers, [int(year) for year in bin_centers], rotation=0)
    
    # Add mean and median lines
    mean_year = np.mean(year_data)
    median_year = np.median(year_data)
    plt.axvline(mean_year, color='red', linestyle='--', label=f'Mean Year: {mean_year:.1f}')
    plt.axvline(median_year, color='orange', linestyle='--', label=f'Median Year: {median_year:.1f}')
    
    # Customize plot
    plt.title(title)
    plt.xlabel('Year of Manufacturing')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Add statistics box
    stats_text = (f'Total Count: {len(year_data)}\n'
                 f'Earliest Year: {int(min(year_data))}\n'
                 f'Latest Year: {int(max(year_data))}\n'
                 f'Range: {int(max(year_data) - min(year_data))} years')
    
    plt.text(0.02, 0.98, stats_text,
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()