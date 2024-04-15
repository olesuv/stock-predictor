import data_pre_processing as dpp
import model as m


if __name__ == '__main__':
    dpp = dpp.DataPreProcessing()
    dpp.load_data('data')
    dpp.process_stock_data('bitcoin')
    stock = dpp.get_stock_data('bitcoin')
    print(stock)

    # model = m.StockPredictor()
    # model.load_data(stock)
    # model.benchamrk_model()
