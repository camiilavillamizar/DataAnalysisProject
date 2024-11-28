
import seaborn as sns
import matplotlib.pyplot as plt

def plot(probs, title):
    sns.heatmap(probs, annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title(title)
    plt.show()