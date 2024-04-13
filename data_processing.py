import glob
import pandas as pd


class DataPreProcessing:
    """
    This class represents a data pre-processing utility for handling CSV files.
    It provides methods to read CSV files from a specified directory and store them
    in a dictionary, as well as retrieve the stored data.

    Attributes:
        file_path (str): The path to the directory containing the CSV files.
        data (dict): A dictionary containing the CSV file names as keys and the
        corresponding pandas dataframes as values.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = None

    def process_data(self) -> None:
        """
        This method reads the CSV files from the data folder and stores them
        in a dictionary with the file name as the key and the pandas dataframe
        as the value. (NOT IMPLEMENTED YET)
        """
        df = {}
        csv_files = glob.glob(self.path + "/*.csv")

        for file in csv_files:
            crypto_csv = pd.read_csv(file)
            df[file] = crypto_csv

        self.data = df

    def get_data(self) -> dict:
        """
        This method returns the dictionary containing the data.
        """
        return self.data
