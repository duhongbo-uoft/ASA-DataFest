## Author: Hongbo Du

import pandas_datareader as pdr
import pandas as pd
import datetime
import requests

# Loading stock data
JD = pdr.get_data_yahoo("JD", 
                        start = datetime.datetime(2015, 6, 1), 
                        end = datetime.datetime(2020, 6, 10))

AMZN = pdr.get_data_yahoo("AMZN", 
                        start = datetime.datetime(2015, 6, 1), 
                        end = datetime.datetime(2020, 6, 10))

SHOP = pdr.get_data_yahoo("SHOP", 
                        start = datetime.datetime(2015, 6, 1), 
                        end = datetime.datetime(2020, 6, 10))

BABA = pdr.get_data_yahoo("BABA", 
                        start = datetime.datetime(2015, 1, 1), 
                        end = datetime.datetime(2020, 6, 10))

EBAY = pdr.get_data_yahoo("EBAY", 
                        start = datetime.datetime(2015, 6, 1), 
                        end = datetime.datetime(2020, 6, 10))

WMT = pdr.get_data_yahoo("WMT",
                        start = datetime.datetime(2015, 6, 1),
                        end = datetime.datetime(2020, 6, 10))

PDD = pdr.get_data_yahoo("PDD",
                        start = datetime.datetime(2015, 6, 1),
                        end = datetime.datetime(2020, 6, 10))

stock_dataset = [JD['Close'], AMZN['Close'], SHOP['Close'], BABA['Close'], EBAY['Close'], WMT['Close'], PDD['Close']]

# Specifying training and testing dataset
JD_train, JD_test = JD['Close'].loc['2015-06-01':'2020-03-01'], JD['Close'].loc['2020-03-01':]
AMZN_train, AMZN_test = AMZN['Close'].loc['2015-06-01':'2020-03-01'], AMZN['Close'].loc['2020-03-01':]
SHOP_train, SHOP_test = SHOP['Close'].loc['2015-06-01':'2020-03-01'], SHOP['Close'].loc['2020-03-01':]
BABA_train, BABA_test = BABA['Close'].loc['2015-06-01':'2020-03-01'], BABA['Close'].loc['2020-03-01':]
PDD_train, PDD_test = PDD['Close'].loc['2015-06-01':'2020-03-01'], PDD['Close'].loc['2020-03-01':]
EBAY_train, EBAY_test = EBAY['Close'].loc['2015-06-01':'2020-03-01'], EBAY['Close'].loc['2020-03-01':]
WMT_train, WMT_test = WMT['Close'].loc['2015-06-01':'2020-03-01'], WMT['Close'].loc['2020-03-01':]

train_set = [JD_train, AMZN_train, SHOP_train, BABA_train, PDD_train, EBAY_train, WMT_train]
test_set = [JD_test, AMZN_test, SHOP_test, BABA_test, PDD_test, EBAY_test, WMT_test]

# Loading COVID-19 data
covid19_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/ecdc/full_data.csv'
covid19_raw = pd.read_csv(covid19_url, error_bad_lines=False)
covid19_adj = covid19_raw.set_index("location", drop = True)

CAN = covid19_adj.loc['Canada':'Canada', 'date':'total_deaths']
CHN = covid19_adj.loc['China':'China', 'date':'total_deaths']
USA = covid19_adj.loc['United States':'United States', 'date':'total_deaths']

COVID19_dataset = [CAN, CHN, USA]

CHN['total_cases'].plot(figsize = (18, 3), grid = True)
plt.show()
CAN['total_cases'].plot(figsize = (18, 3), grid = True)
plt.show()
