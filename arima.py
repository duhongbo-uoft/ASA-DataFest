## Author: Hongbo Du

import autograd.numpy as np
import autograd.numpy.random as npr
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from LoadingData.py import stock_dataset
import os
os.system('LoadingData.py')

# ARIMA Forecasts
def fit_arima(train_data, test_data):

    # fit ARIMA(1, 1, 0) model
    arima_model = ARIMA(np.log(train_data), (1, 1, 0))
    fitted_model = arima_model.fit()

    # print summary
    print(fitted_model.summary())

    # make forecast
    forecast_val, se, ci = fitted_model.forecast(len(test_data))
    forecast_series = pd.Series(np.exp(forecast_val), index = test_data.index)
    lower_bound = pd.Series(np.exp(ci[:, 0]), index = test_data.index)
    upper_bound = pd.Series(np.exp(ci[:, 1]), index = test_data.index)

    # combine results
    res_list = [forecast_series, lower_bound, upper_bound]
    return res_list


def make_plt(train_data, test_data, forecast_data):
    # initalize plot
    plt.figure(figsize=(18,3))

    plt.plot(train_data, label = 'original time series')
    plt.plot(test_data, label = 'testing time series')
    plt.plot(forecast_data[0], label = 'forecast')
    plt.fill_between(forecast_data[1].index, forecast_data[1], forecast_data[2], 
                     color='k', alpha=.15)

def make_forecast(original_data):
        # fit ARIMA(1, 1, 0) model
    arima_model = ARIMA(np.log(original_data), (1, 1, 0))
    fitted_model = arima_model.fit()

    # print summary
    print(fitted_model.summary())

    # make forecast
    forecast_val, se, ci = fitted_model.forecast(90)
    forecast_series = pd.Series(np.exp(forecast_val), index = original_data.index[-1] + pd.to_timedelta(np.arange(90), 'D'))
    lower_bound = pd.Series(np.exp(ci[:, 0]), index = original_data.index[-1] + pd.to_timedelta(np.arange(90), 'D'))
    upper_bound = pd.Series(np.exp(ci[:, 1]), index = original_data.index[-1] + pd.to_timedelta(np.arange(90), 'D'))

    # combine results
    res_list = [forecast_series, lower_bound, upper_bound]
    return res_list

def make_forecast_plt(original_data, forecast_data):
    plt.figure(figsize=(10,6))
    plt.plot(original_data, label = 'original time series')
    plt.plot(forecast_data[0], label = 'forecast')
    plt.fill_between(forecast_data[1].index, forecast_data[1], forecast_data[2], 
                     color='k', alpha=.15)
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('stock price')

if __name__ == "__main__":
    for i in range(len(train_set)):
        data_train, data_test = train_set[i], test_set[i]
        data_forecast = fit_arima(data_train, data_test)
        make_plt(data_train, data_test, data_forecast) # forecast vs test data
    
    for i in range(len(stock_dataset)):
        original_data, forecast_init = stock_dataset[i], stock_dataset[i].loc['2020-03-01':]
        data_forecast = make_forecast(original_data)
        make_forecast_plt(original_data, data_forecast)



