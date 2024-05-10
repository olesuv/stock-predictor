import time
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


class StockPredictor:
    """
    A class for predicting stock prices using linear regression.

    Attributes:
        llr (LinearRegression): The linear regression model.
        train_time (float): The time taken to train the model.

    Methods:
        train(x_train, y_train): Trains the model using the given training data.
        predict(x_pred): Predicts the stock prices using the trained model.
        benchmark(y_train, y_pred): Prints the evaluation metrics for the model.
        mape(a, b): Calculates the mean absolute percentage error between two arrays.
        plot(x_train, y_train, y_pred): Plots the actual and predicted stock prices.
    """

    def __init__(self) -> None:
        self.llr = LinearRegression(
            copy_X=True, fit_intercept=True, n_jobs=-1)
        self.train_time = None

    def train(self, x_train, y_train) -> None:
        """
        Trains the model using the given training data.

        Args:
            x_train (array-like): The input features for training.
            y_train (array-like): The target values for training.

        Returns:
            None
        """
        start = time.time()
        self.llr.fit(x_train, y_train)
        end = time.time()
        self.train_time = end - start

    def predict(self, x_pred) -> np.ndarray:
        """
        Predicts the stock prices using the trained model.

        Args:
            x_pred (array-like): The input features for prediction.

        Returns:
            np.ndarray: The predicted stock prices.
        """
        y_pred = self.llr.predict(x_pred)
        return y_pred

    def benchmark(self, y_train, y_pred) -> None:
        """
        Prints the evaluation metrics for the model.

        Args:
            y_train (array-like): The actual target values.
            y_pred (array-like): The predicted target values.

        Returns:
            None
        """
        train_mse = mean_squared_error(y_train, y_pred)
        train_r2 = r2_score(y_train, y_pred)
        train_mape = self.mape(y_train, y_pred)

        print()
        print(f"Train time: {self.train_time} seconds")
        print(f"Train MSE: {train_mse:.2f}")
        print(f"Train R2: {train_r2:.2%}")
        print(f"Train MAPE: {train_mape:.2%}")

    def mape(self, a, b) -> float:
        """
        Calculates the mean absolute percentage error between two arrays.

        Args:
            a (array-like): The first array.
            b (array-like): The second array.

        Returns:
            float: The mean absolute percentage error.
        """
        mask = a != 0
        absolute_percentage_errors = np.abs(
            (a - b) / np.maximum(np.abs(a), 1e-8))
        return absolute_percentage_errors[mask].mean()

    def plot(self, x_train, y_train, y_pred) -> None:
        """
        Plots the actual and predicted stock prices.

        Args:
            x_train (array-like): The input features for training.
            y_train (array-like): The actual target values.
            y_pred (array-like): The predicted target values.

        Returns:
            None
        """
        df_pred = pd.DataFrame(
            {'Actual': y_train, 'Predicted': y_pred, 'Date': x_train[:, 0]})
        df_pred.sort_values(by='Date', inplace=True)
        print()
        print(df_pred)

        plt.plot(df_pred['Date'], df_pred['Actual'], label='Actual')
        plt.plot(df_pred['Date'], df_pred['Predicted'], label='Predicted')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title('Actual vs Predicted')
        plt.legend()
        plt.show()
