# Yahoo Finance API

Minimal API to interact with Yahoo Finance.

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
    sys.exit(-1)

print(symbol_data)
```
