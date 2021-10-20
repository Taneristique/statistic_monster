import pandas as pd 
import json 
from binance.client import Client
from scipy.stats import zscore

def z__score():
    with open('config.json') as jsonfile:
        file=json.load(jsonfile)
        jsonfile.close()
    client=Client(file['api_key'], ['api_secret'])

    x=pd.DataFrame(client.get_ticker())
    coin_list=x[x.symbol.str.contains('USDT')]
    coin_list.sort_values(by='priceChangePercent',ascending=False)
    print(x)

    symbol=input('please chose any symbol from the ticker\n')

    frame=pd.DataFrame(client.get_klines(symbol=symbol,interval='1d'))
    frame = frame.iloc[:,:6]  
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index,unit='ms')
    frame=frame.astype('float')

    print(frame)
    z=frame.apply(zscore)
    print("Z-score applied to tading pair.Here you wiil see z-score for every column and row of asset's matrix:")
    print(z)


