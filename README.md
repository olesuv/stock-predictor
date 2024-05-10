## Predict your favourite crypto price (in availbale date range)

Project is only code based (no ui or terminal commands) and focused on building regresion model for crypto u will choose.
For detailed data research and model research check files: `data_research.ipynb` and `model_research.ipynb`.

## Input

Go to `~/main.py` and on 8 row selelct your crypto from `~/data/`. Example:

```python
dpp.process_whole_stock_data('bitcoin')
```

## Output

Returns training / prediction metricks and plots diagram for check data correctness. Example output:

```console
(venv) ➜  stock-predictor git:(main) python3 main.py

Train time: 0.0047833919525146484 seconds
Train MSE: 76490.93
Train R2: 99.96%
Train MAPE: 22.50%

       Actual     Predicted      Date
0         0.1     -0.599570 -1.731659
1         0.1     -0.650913 -1.730875
2         0.1     -0.649552 -1.730092
3         0.1     -0.648234 -1.729308
4         0.1     -0.647001 -1.728524
...       ...           ...       ...
4415  20831.3  21607.906886  1.728524
4416  21138.9  21170.545010  1.729308
4417  21517.2  21491.744238  1.730092
4418  21416.3  21032.574638  1.730875
4419  21309.0  21252.596035  1.731659
```

![example output plot for bitcoin](assets/bitcoin.png "Exmaple output (Bitcoin)")
