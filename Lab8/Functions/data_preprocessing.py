# Functions/data_preprocessing.py

def clean_data(df):
    # Example: Remove rows with any NaN values
    df.dropna(inplace=True)
    return df
