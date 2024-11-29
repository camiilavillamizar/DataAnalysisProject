from exploring_relationships.plot_relationship import plot

def getRelationshipBirthsAndOccurrences(df):
    # Clean the `births` column by removing commas and converting to numeric
    df['births'] = df['births'].replace({',': ''}, regex=True).astype(float)

    # Check for missing values in the columns of interest
    print(df[['occurrences', 'births']].isnull().sum())

    # Drop rows with missing values in `occurrences` or `births`
    df_cleaned = df[['occurrences', 'births']].dropna()

    # Calculate the correlation
    correlation = df_cleaned['occurrences'].corr(df_cleaned['births'])
    print(f"Correlation between occurrences and births: {correlation:.4f}")

    plot(df_cleaned, "births", "Scatter Plot of Occurrences vs Births", 
         "Number of Births", "Number of Occurrences")