import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def plot_frequency(data_list, title="", figsize=(10, 6), 
                  color='skyblue', edgecolor='navy', ylabel="Frequency", 
                  xlabel="Values", rotation=45, limit=-1):
    """
    Creates a column chart showing the frequency of unique values in a list,
    sorted in decreasing order of frequency.
    
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
    
    # Sort the counter items by frequency in descending order
    sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    if limit != -1:
        sorted_items = sorted_items[:limit]
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