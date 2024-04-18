import datetime as dt
import numpy as np
import data_pre_processing as dpp
import model as m

from sklearn.discriminant_analysis import StandardScaler


if __name__ == '__main__':
    user_input = {
        'Date': '2022-08-24',
        'Open': 22465.5,
        'High': 22974.0,
        'Low': 22306.8,
        'Volume': 240218
    }
    ordinal_date = dt.datetime.strptime(
        user_input['Date'], '%Y-%m-%d').date().toordinal()
    user_input['Date'] = ordinal_date
    user_input = np.array(list(user_input.values())).reshape(1, -1)

    scaler = StandardScaler()
    user_input = scaler.fit_transform(user_input)

    dpp = dpp.DataPreProcessing()
    dpp.load_data('data')
    dpp.process_whole_stock_data('bitcoin')
    dpp.standardize_data()

    model = m.StockPredictor()
    model.train(dpp.x_train, dpp.y_train)
    y_pred = model.predict(user_input)
    print(y_pred)  # real close price: $22,609.16

    # model.benchmark(dpp.y_train, y_pred)
    # model.plot(dpp.x_train, dpp.y_train, y_pred)
