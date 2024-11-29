
from exploring_relationships.plot_relationship import plot

def getRelationshipBetweenDollarExchangeAndOccurrences(df):
    # Clean the `dollar_exchange` column if it contains any formatting issues (e.g., commas or invalid characters)
    df['dollar_exchange'] = df['dollar_exchange'].replace({',': ''}, regex=True).astype(float)

    # Check for missing values in the columns of interest
    print(df[['occurrences', 'dollar_exchange']].isnull().sum())

    # Drop rows with missing values in `occurrences` or `dollar_exchange`
    df_cleaned = df[['occurrences', 'dollar_exchange']].dropna()

    # Calculate the correlation
    correlation = df_cleaned['occurrences'].corr(df_cleaned['dollar_exchange'])
    print(f"Correlation between occurrences and dollar_exchange: {correlation:.4f}")

    plot(df_cleaned, "dollar_exchange", "Scatter Plot of Occurrences vs Dollar Exchange Rate", 
         "Dollar Exchange Rate", "Number of Occurrences")
