# Module for loading and cleaning data.

import pandas as pd
from typing import Optional

class DataLoader:

    def __init__(self, filepath: str):
        """
        Args:
            filepath (str): Path to the data file.
        """
        self.filepath = filepath
        self.data: Optional[pd.DataFrame] = None

    def load(self) -> pd.DataFrame:
        """
        Loads the CSV file into a DataFrame.

        Returns:
            pd.DataFrame: Loaded data.
        """
        self.data = pd.read_csv(self.filepath)
        return self.data

    def clean(self) -> pd.DataFrame:
        """
        Cleans the loaded data (e.g., handling missing values).

        Returns:
            pd.DataFrame: Cleaned data.
        """
        if self.data is None:
            raise ValueError("Data not loaded yet")
        # Example: drop rows with missing values
        self.data = self.data.dropna()
        return self.data