# Yahoo Finance API

Minimal API to interact with Yahoo Finance.

## Installation

```
pip install yahoo_finance_api2
```

## Usage

The following example retrieves 10 days of 5 minute frequency Microsoft (MSFT) stock data.

```
import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

my_share = share.Share('MSFT')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          10,
                                          share.FREQUENCY_TYPE_MINUTE,
                                          5)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

print(symbol_data)
```

The output format:

```
{
  'timestamp': [...],
  'open': [...],
  'high': [...],
  'low': [...],
  'close': [...],
  'volume': [...]
}
```

## API

* Class `Share`:
  * `get_historical(period_type, period, frequency_type, frequency)`
    * Returns historical data for the given period type (`share.PERIOD_TYPE_DAY`, `share.PERIOD_TYPE_WEEK`, `share.PERIOD_TYPE_MONTH`, `share.PERIOD_TYPE_YEAR`), period (1, 5, 10, etc.), frequency_type (`share.FREQUENCY_TYPE_MINUTE`, `share.FREQUENCY_TYPE_DAY`, `share.FREQUENCY_TYPE_MONTH`, `share.FREQUENCY_TYPE_YEAR`), and frequency (1, 5, 10, etc.). Only certain combinations of these parameters are allowed.
