import time
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


class StockPredictor:
    def __init__(self) -> None:
        self.llr = LinearRegression(
            copy_X=True, fit_intercept=True, n_jobs=-1)
        self.train_time = None

    def train(self, x_train, y_train) -> np.ndarray:
        start = time.time()

        self.llr.fit(x_train, y_train)
        y_pred = self.llr.predict(x_train)

        end = time.time()
        self.train_time = end - start

        return y_pred

    def benchmark(self, y_train, y_pred) -> None:
        train_mse = mean_squared_error(y_train, y_pred)
        train_r2 = r2_score(y_train, y_pred)
        train_mape = self.mape(y_train, y_pred)

        print()
        print(f"Train time: {self.train_time} seconds")
        print(f"Train MSE: {train_mse:.2f}")
        print(f"Train R2: {train_r2:.2%}")
        print(f"Train MAPE: {train_mape:.2%}")

    def mape(self, a, b) -> float:
        mask = a != 0
        absolute_percentage_errors = np.abs(
            (a - b) / np.maximum(np.abs(a), 1e-8))
        return absolute_percentage_errors[mask].mean()
