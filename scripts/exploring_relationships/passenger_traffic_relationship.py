
from exploring_relationships.plot_relationship import plot

def getRelationshipBetweenPassengerTrafficAndOccurrences(df):
    # Clean the `passenger_traffic` column by converting to numeric (in case of any formatting issues)
    df['passenger_traffic'] = df['passenger_traffic'].replace({',': ''}, regex=True).astype(float)

    # Check for missing values in the columns of interest
    print(df[['occurrences', 'passenger_traffic']].isnull().sum())

    # Drop rows with missing values in `occurrences` or `passenger_traffic`
    df_cleaned = df[['occurrences', 'passenger_traffic']].dropna()

    # Calculate the correlation
    correlation = df_cleaned['occurrences'].corr(df_cleaned['passenger_traffic'])
    print(f"Correlation between occurrences and passenger traffic: {correlation:.4f}")

    plot(df_cleaned, "passenger_traffic", 
         "Scatter Plot of Occurrences vs Passenger Traffic", 
         "Passenger Traffic", "Number of Occurrences")

