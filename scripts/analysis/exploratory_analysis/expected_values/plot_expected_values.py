import matplotlib.pyplot as plt

def plot(df, title, ylabel, xlabel):
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', color='mediumseagreen', edgecolor='black')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
