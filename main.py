import model.data_pre_processing as dpp
import model.model as m


if __name__ == '__main__':
    dpp = dpp.DataPreProcessing()
    dpp.load_data('data')
    dpp.process_whole_stock_data('bitcoin')
    dpp.standardize_data()

    model = m.StockPredictor()
    model.train(dpp.x_train, dpp.y_train)
    y_pred = model.predict(dpp.x_train)

    model.benchmark(dpp.y_train, y_pred)
    model.plot(dpp.x_train, dpp.y_train, y_pred)
