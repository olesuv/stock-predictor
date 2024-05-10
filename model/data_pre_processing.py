import datetime as dt
import pandas as pd
import glob
import os

from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split


class DataPreProcessing:
    """
    A class for data pre-processing in stock prediction.

    Methods:
    - load_data(file_path: str) -> None: Loads the data from the specified file path.
    - process_stock_data(stock_name: str): Processes the stock data for a specific stock.
    - process_whole_stock_data(stock_name: str): Processes the entire stock data for a specific stock.
    - get_stock_data(stock_name: str) -> pd.DataFrame: Retrieves the stock data for a specific stock.
    - standardize_data() -> None: Standardizes the data.
    - get_stocks_data() -> dict: Retrieves the loaded stock data.
    """

    def __init__(self) -> None:
        pass

    def load_data(self, file_path: str) -> None:
        """
        Loads the data from the specified file path.

        Args:
        - file_path (str): The path to the directory containing the CSV files.

        Raises:
        - FileNotFoundError: If the specified file path does not exist.
        - FileNotFoundError: If no CSV files are found in the directory.
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

            crypto_csv['Date'] = pd.to_datetime(crypto_csv['Date'])
            crypto_csv['Date'] = crypto_csv['Date'].map(dt.datetime.toordinal)

            crypto_name = file.split('/')[-1].split('.')[0]
            df_cryptos[crypto_name] = crypto_csv.sort_values(
                'Date', ascending=True)

        self.data = df_cryptos

    def process_stock_data(self, stock_name: str):
        """
        Processes the stock data for a specific stock.

        Args:
        - stock_name (str): The name of the stock.

        Raises:
        - ValueError: If the specified stock name is not found in the data.
        """

        stock_data = self.get_stock_data(stock_name)
        self.x = stock_data[['Date', 'Open', 'High', 'Low', 'Volume']]
        self.y = stock_data['Close']

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.x, self.y, test_size=0.2, random_state=42)

    def process_whole_stock_data(self, stock_name: str):
        """
        Processes the entire stock data for a specific stock.

        Args:
        - stock_name (str): The name of the stock.

        Raises:
        - ValueError: If the specified stock name is not found in the data.
        """

        stock_data = self.get_stock_data(stock_name)
        self.x = stock_data[['Date', 'Open', 'High', 'Low', 'Volume']]
        self.y = stock_data['Close']

        self.x_train = self.x
        self.x_test = None
        self.y_train = self.y
        self.y_test = None

    def get_stock_data(self, stock_name: str) -> pd.DataFrame:
        """
        Retrieves the stock data for a specific stock.

        Args:
        - stock_name (str): The name of the stock.

        Returns:
        - pd.DataFrame: The stock data for the specified stock.

        Raises:
        - ValueError: If the specified stock name is not found in the data.
        """

        if stock_name not in self.data:
            raise ValueError(f"{stock_name} not found in the data.")

        return self.data[stock_name]

    def standardize_data(self) -> None:
        """
        Standardizes the data.

        Raises:
        - ValueError: If the data has not been processed yet.
        """

        if hasattr(self, 'x_train') and self.x_test == None:
            scaler = StandardScaler()
            self.x_train = scaler.fit_transform(self.x_train)
            return
        if not hasattr(self, 'x_train') or not hasattr(self, 'x_test'):
            raise ValueError(
                "Data not processed. Call 'process_stock_data' first.")

        scaler = StandardScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)

    def get_stocks_data(self) -> dict:
        """
        Retrieves the loaded stock data.

        Returns:
        - dict: The loaded stock data.

        Raises:
        - ValueError: If the data has not been loaded yet.
        """

        if not hasattr(self, 'data'):
            raise ValueError("Data not loaded. Call 'load_data' first.")
