import pandas as pd
import glob
import os


class DataPreProcessing:
    """
    A class for loading and preprocessing data for stock prediction.

    Attributes:
        path (str): The path to the directory containing the CSV files.
        data (pd.DataFrame): The preprocessed data.

    Methods:
        load_data(file_path: str) -> None: Loads the data from the specified file path.
        get_data() -> dict: Returns the preprocessed data.
    """

    def __init__(self) -> None:
        self.path = None
        self.data = None

    def load_data(self, file_path: str) -> None:
        """
        Loads the data from the specified file path.

        Args:
            file_path (str): The path to the directory containing the CSV files.

        Raises:
            FileNotFoundError: If the specified path does not exist.
            FileNotFoundError: If no CSV files are found in the directory.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Path '{file_path}' does not exist.")
        self.path = file_path

        df_cryptos = {}

        csv_files = glob.glob(f"{self.path}/*.csv")
        csv_files = [file for file in csv_files if not file.endswith(
            'Current Crypto leaderboard.csv')]

        if not csv_files:
            raise FileNotFoundError("No CSV files found in the directory.")

        for file in csv_files:
            crypto_csv = pd.read_csv(file)
            crypto_name = file.split('/')[-1].split('.')[0]
            df_cryptos[crypto_name] = crypto_csv.sort_values(
                'Date', ascending=True)

        self.data = df_cryptos

    def get_data(self) -> dict:
        """
        Returns the preprocessed data.

        Returns:
            dict: The preprocessed data.
        """
        return self.data
