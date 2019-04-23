import pprint
import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

my_share = share.Share('NBR')
symbol_data = None

try:
    symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                          10,
                                          share.FREQUENCY_TYPE_MINUTE,
                                          5)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(symbol_data)
