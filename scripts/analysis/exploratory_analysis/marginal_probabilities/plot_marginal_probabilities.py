import matplotlib.pyplot as plt
from analysis.exploratory_analysis.constants_exploratory_analysis import COLOR_PALETTE, DEFAULT_COLOR

def plot(df, title, ylabel, xlabel, titleLegend = None):
    color = DEFAULT_COLOR if titleLegend is None else COLOR_PALETTE
    df.plot(kind='bar', stacked=True, figsize=(10, 6), color=color, edgecolor='black')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=45)
    if titleLegend is not None: 
        plt.legend(title=titleLegend, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()