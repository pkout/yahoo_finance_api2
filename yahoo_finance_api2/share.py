import datetime
import pprint
import requests
import yaml
from yahoo_finance_api2.exceptions import YahooFinanceError

PERIOD_TYPE_DAY = 'day'
PERIOD_TYPE_WEEK = 'week'
PERIOD_TYPE_MONTH = 'month'
PERIOD_TYPE_YEAR = 'year'

# Valid frequencies: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
FREQUENCY_TYPE_MINUTE = 'm'
FREQUENCY_TYPE_DAY = 'd'
FREQUENCY_TYPE_WEEK = 'wk'
FREQUENCY_TYPE_MONTH = 'mo'

class Share(object):

    def __init__(self, symbol):
        self.symbol = symbol


    def get_historical(self, period_type, period, frequency_type, frequency):
        data = self._download_symbol_data(period_type, period,
                                          frequency_type, frequency)

        valid_frequency_types = [
            FREQUENCY_TYPE_MINUTE, FREQUENCY_TYPE_DAY,
            FREQUENCY_TYPE_WEEK, FREQUENCY_TYPE_MONTH
        ]

        if frequency_type not in valid_frequency_types:
            raise ValueError('Invalid frequency type: ' % frequency_type)

        # for i in range(len(data['timestamp'])):
        #     if i < (len(data['timestamp']) - 1):
        #         print(datetime.datetime.utcfromtimestamp(
        #                 data['timestamp'][i + 1]
        #             ).strftime('%Y-%m-%d %H:%M:%S'),
        #             data['timestamp'][i + 1] - data['timestamp'][i]
        #         )

        if 'timestamp' not in data:
            return None

        return_data = {
            'timestamp': [x * 1000 for x in data['timestamp']],
            'open': data['indicators']['quote'][0]['open'],
            'high': data['indicators']['quote'][0]['high'],
            'low': data['indicators']['quote'][0]['low'],
            'close': data['indicators']['quote'][0]['close'],
            'volume': data['indicators']['quote'][0]['volume']
        }

        return return_data


    def _set_time_frame(self, periodType, period):
        now = datetime.datetime.now()

        if periodType == PERIOD_TYPE_DAY:
            period = min(period, 59)
            start_time = now - datetime.timedelta(days=period)
        elif periodType == PERIOD_TYPE_WEEK:
            period = min(period, 59)
            start_time = now - datetime.timedelta(days=period * 7)
        elif periodType == PERIOD_TYPE_MONTH:
            period = min(period, 59)
            start_time = now - datetime.timedelta(days=period * 30)
        elif periodType == PERIOD_TYPE_YEAR:
            period = min(period, 59)
            start_time = now - datetime.timedelta(days=period * 365)
        else:
            raise ValueError('Invalid period type: ' % periodType)

        end_time = now

        return start_time.strftime("%s"), end_time.strftime("%s")


    def _download_symbol_data(self, period_type, period,
                              frequency_type, frequency):
        start_time, end_time = self._set_time_frame(period_type, period)
        url = (
            'https://query1.finance.yahoo.com/v8/finance/chart/{0}?symbol={0}'
            '&period1={1}&period2={2}&interval={3}&'
            'includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&'
            'region=US&crumb=t5QZMhgytYZ&corsDomain=finance.yahoo.com'
        ).format(self.symbol, start_time, end_time,
                 self._get_frequency_str(frequency_type, frequency))

        resp_json = requests.get(url).json()

        if self._is_yf_response_error(resp_json):
            self._raise_yf_response_error(resp_json)
            return

        data_json = resp_json['chart']['result'][0]

        return data_json


    def _is_yf_response_error(self, resp):
        return resp['chart']['error'] is not None


    def _raise_yf_response_error(self, resp):
        raise YahooFinanceError(
            '{0}: {1}'.format(
                resp['chart']['error']['code'],
                resp['chart']['error']['description']
            )
        )

    def _get_frequency_str(self, frequency_type, frequency):
        return '{1}{0}'.format(frequency_type, frequency)
