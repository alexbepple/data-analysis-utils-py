import pandas as pd
from .pyfolio import deposit

def create_daily_series(start_dt, values):
    daily_index = pd.date_range(start_dt, periods=len(values), freq='D')
    return pd.Series(values, index=daily_index)

class TestDeposit(object):
    def test_increments_following_amounts(self):
        series = create_daily_series('2000-01-01', [0, 1])
        pd.testing.assert_series_equal(
            deposit('2000-01-01', 1, series), 
            series + 1
        )
    
    def test_does_not_increment_preceding_amounts(self):
        series = create_daily_series('2000-01-01', [0])
        assert deposit('2000-01-02', 1, series)['2000-01-01'] == 0

    def test_adds_entry_for_deposit(self):
        series = create_daily_series('2000-01-01', [0])
        assert deposit('1999-12-31', 1, series)[pd.to_datetime('1999-12-31')] == 1

    def test_adds_to_the_amount_on_the_deposit_day(self):
        series = create_daily_series('2000-01-01', [1])
        assert deposit('2000-01-01', 1, series).values == [2]

    def test_does_not_add_intermediate_values(self):
        series = create_daily_series('2000-01-03', [0])
        with_deposit = deposit('2000-01-01', 1, series)
        dt_in_between = pd.to_datetime('2000-01-02')
        assert dt_in_between not in with_deposit.index
