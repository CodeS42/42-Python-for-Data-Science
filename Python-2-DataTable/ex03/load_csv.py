import pandas as pd
from pandas import DataFrame

def load(path: str) -> DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    The function prints its dimensions and return the DataFrame.

    If an error occurs, the error is printed and the function returns None.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
