from catboost import CatBoostRegressor
from common.export_temp_csv import export_csv_temp
import pandas as pd

def predict_year_of_manuf(df):
    #Separating rows with YearOfManuf == 0 (to predict) and others (to train)
    train = df[df["YearOfManuf"] != 0]
    test = df[df["YearOfManuf"] == 0]

    #Features and target
    X = train.drop(columns=["YearOfManuf"])
    y = train["YearOfManuf"]
    X_test = test.drop(columns=["YearOfManuf"])

    #Handling datetime columns
    datetime_columns = X.select_dtypes(include=["datetime64", "datetime"]).columns
    for col in datetime_columns:
        # Converting datetime columns to numerical (days since the earliest date)
        earliest_date = pd.to_datetime(X[col].min())
        X[col] = (pd.to_datetime(X[col]) - earliest_date).dt.days
        X_test[col] = (pd.to_datetime(X_test[col]) - earliest_date).dt.days

    #Converting object columns to string for CatBoost compatibility
    categorical_columns = X.select_dtypes(include=["object"]).columns
    X[categorical_columns] = X[categorical_columns].astype(str)
    X_test[categorical_columns] = X_test[categorical_columns].astype(str)

    #Checking for any remaining incompatible columns
    numeric_columns = X.select_dtypes(include=["number"]).columns
    for col in X.columns:
        if col not in numeric_columns and col not in categorical_columns:
            print(f"Dropping incompatible column: {col}")
            X = X.drop(columns=[col])
            X_test = X_test.drop(columns=[col])
    
    #Training the CatBoost model
    model = CatBoostRegressor(cat_features=categorical_columns.tolist(), verbose=0, random_state=42)
    model.fit(X, y)

    #Filter rows where YearOfManuf was 0 and update them with predicted values
    generated_years_df = test.copy()
    generated_years_df["YearOfManuf"] = model.predict(X_test).astype(int)

    # Adjust predictions based on OccDate
    generated_years_df["OccYear"] = pd.to_datetime(generated_years_df["OccDate"]).dt.year
    generated_years_df.loc[
        generated_years_df["YearOfManuf"] >= generated_years_df["OccYear"], 
        "YearOfManuf"
    ] = generated_years_df["OccYear"] - 1

    #Drop temporary column
    generated_years_df = generated_years_df.drop(columns=["OccYear"])

    export_csv_temp(generated_years_df, "0_years_filled")