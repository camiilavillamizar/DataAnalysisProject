
import seaborn as sns
import matplotlib.pyplot as plt

def plot(df_cleaned, x, title, xlabel, ylabel):
    # Visualize the correlation with a scatter plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x, y='occurrences', data=df_cleaned, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(alpha=0.5)
    plt.show()

    # Visualize with a heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(df_cleaned.corr(), annot=True, cmap='coolwarm', fmt=".4f", cbar=True)
    plt.title('Correlation Heatmap')
    plt.show()