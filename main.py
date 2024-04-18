import data_pre_processing as dpp
import model as m


if __name__ == '__main__':
    user_input = {
        'Date': '2022-08-24',
        'Open': 22465.5,
        'High': 22974.0,
        'Low': 22306.8,
        'Volume': 240218
    }
    # real close price: $22,609.16

    dpp = dpp.DataPreProcessing()
    dpp.load_data('data')
    dpp.process_whole_stock_data('bitcoin')
    dpp.standardize_data()

    model = m.StockPredictor()
    model.train(dpp.x_train, dpp.y_train)
    y_pred = model.predict(dpp.x_train)
    model.benchmark(dpp.y_train, y_pred)
    model.plot(dpp.x_train, dpp.y_train, y_pred)
