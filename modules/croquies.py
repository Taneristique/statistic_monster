"""// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Taneristique"""

import matplotlib.pyplot as plt
import pandas as pd 
import json
import numpy as np
import plotly.graph_objects as go
from binance.client import Client
from time import sleep
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score

def make_croquie():
    with open('config.json') as jsonfile:
        file=json.load(jsonfile)
        jsonfile.close()
    client=Client(file['api_key'], ['api_secret'])

    x=pd.DataFrame(client.get_ticker())
    coin_list=x[x.symbol.str.contains('USDT')]
    coin_list.sort_values(by='priceChangePercent',ascending=False)


    print('select the coin you want to trade')
    sym=input()


    frame=pd.DataFrame(client.get_klines(symbol=sym,interval='1d'))
    frame = frame.iloc[:,:6]  
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index,unit='ms')
    frame=frame.astype('float')

    def macd(lengthrapide,lengthslow,signal):
        frame['emarapide']=frame.Close.ewm(span=lengthrapide,adjust=False).mean()
        frame['emaslow']=frame.Close.ewm(span=lengthslow,adjust=False).mean()
        frame['macd']=frame.emarapide.subtract(frame.emaslow)
        frame['signal']=frame.macd.ewm(span=9,adjust=False).mean()
        print(frame[['macd','signal']])
    macd(13,26,9)
    frame.Close.plot()
    frame=frame.copy()
    sma50=50
    sma200=200
    frame['sma50']=frame.Close.rolling(sma50).mean()
    frame['sma200']=frame.Close.rolling(sma200).mean()
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(frame[['Close','sma50','sma200']])
    frame=frame.dropna() #drop unavailable columns or rows
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(frame[['macd','signal']])

    #nbformat>=4.2.0 is required
    fig = go.Figure(data=[go.Candlestick(x=frame.index,
                        open=frame.Open,
                        high=frame.High,
                        low=frame.Low,
                        close=frame.Close)])
    fig.show()

    x=[frame.Close[i-10] for i in range(len(frame.Close))]
    y=[frame.Close[i] for i in range(len(frame.Close))]
    frame['momentum']=[y[t]-x[t] for t in range(len(x))]
    fig,ax=plt.subplots(figsize=(10,6))
    ax.plot(frame[['momentum']])
    frame

    verify="would you want to compare selected asset with another asset"
    symbol=input('Which symbol?')
    second_kline=pd.DataFrame(client.get_klines(symbol=symbol,interval='1d'))
    second_kline.columns=['Time','Open','High','Low','Close','Volume','emarapide','emaslow','macd','signal','sma50','sma200']
    second_kline=second_kline.set_index('Time')
    second_kline.index=pd.to_datetime(second_kline.index,unit='ms')
    second_kline=second_kline.astype('float')
    source=input('source: Open,Close,High,Low or Volume?')
    if(source!='Open' and source!='Close' and source!='High' and source!='Low' and source!='Volume'):
        source='Close' #default value for source 
    x=np.array(second_kline[source][:100]).reshape(-1,1)
    y=np.array(frame[source][:100]).reshape(-1,1)
    model=linear_model.LinearRegression()
    model.fit(x,y)
    r_sq=model.score(x,y)
    y_predict=model.predict(x)
    print('coefficient of determination r**2 is ',r_sq)
    plt.figure(figsize=(16,9))
    plt.scatter(x,y)
    plt.plot(x, y_predict)
    plt.legend(['regression_line',source])
    plt.title('Cryptocurrency Market Regression Graph')
    plt.xlabel(symbol)
    plt.ylabel(sym)
    plt.show()

    stdx=second_kline[source][:100].std()
    stdy=frame[source][:100].std()


    std_product=stdx*stdy
    cov=np.cov(second_kline[source][:100],frame[source][:100])
    correlation=np.corrcoef(second_kline[source][:100],frame[source][:100],rowvar=False)

    print('standard deviation of '+sym,stdy)
    print('standard deviation of '+symbol,stdx)
    print('the covariance is cov(x,y) = ', cov[0][1])
    print('the product of standard deviations is ',std_product)
    print("the corellation is r = ",correlation[0][1])
    plt.figure(figsize=(16,9))
    plt.scatter(x,y,color='green')
    plt.plot(np.unique(x),np.poly1d(np.polyfit(second_kline[source][:100],frame[source][:100],1))(np.unique(x)),color='blue')
    plt.legend(['regression line','data points'])
    plt.title('Cryptocurrency Market Correlation Graph')
    plt.xlabel(symbol)
    plt.ylabel(sym)
    plt.show()

    print('Did you just realised the last two graph is same because we draw regression graphic according to correlation:)')

    while True:
        ticker=pd.DataFrame(client.get_ticker())
        x=ticker[ticker.symbol.str.contains(sym)]
        print('last price is',float(x.lastPrice.values))
        from time import sleep
        sleep(10)