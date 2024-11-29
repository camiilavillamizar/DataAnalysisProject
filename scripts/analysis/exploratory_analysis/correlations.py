
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.exploratory_analysis.constants_exploratory_analysis import COLUMNS_FOR_HEATMAP, SELECTED_PROVINCES, CATEGORY_MAPPING

def plotCorrelationMatrix(df):
    #Filtering the dataframe
    filtered_df = df[
        (df['CountryID_DisplayEng'] == 'CANADA') &
        (df['ProvinceID_DisplayEng'].isin(SELECTED_PROVINCES))
    ]


    #Creating a numeric dataframe to calculate correlations
    mapped_df = filtered_df[COLUMNS_FOR_HEATMAP].copy()

    for col, mapping in CATEGORY_MAPPING.items():
        mapped_df[col] = filtered_df[col].map(mapping)

    #Correlation matrix
    correlation_matrix = mapped_df.corr()

    #heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap of Selected Variables')
    plt.show()