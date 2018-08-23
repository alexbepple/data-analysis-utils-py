import pandas as pd

def deposit(date, amount, series):
    dt = pd.to_datetime(date)
    extended_index = series.index.union(pd.DatetimeIndex([dt]))
    return pd.concat([
        series + (series.index > dt) * amount,
        pd.Series({dt: amount})
    ]).resample('D').sum().loc[extended_index]
