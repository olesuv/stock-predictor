import data_processing as dp


class StockPredictor:
    def __init__(self) -> None:
        self.data = dp.DataPreProcessing("data")
