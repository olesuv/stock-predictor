import data_pre_processing as dpp
import model as m


if __name__ == '__main__':
    dpp = dpp.DataPreProcessing()
    dpp.load_data('data')
    dpp.process_stock_data('bitcoin')
    stock = dpp.get_stock_data('bitcoin')
    print(stock)

    model = m.StockPredictor()
    y_pred = model.train(x_train=dpp.x_train, y_train=dpp.y_train)
    model.benchmark(y_train=dpp.y_train, y_pred=y_pred)

    # test for commit
