from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import json
class connect:
    def __init__(self):
        with open("config.json") as conf:
            api= json.load(conf)
            conf.close()
        try:
            client = Client(api["api_key"],api["api_secret"])
        except ValueError as e:
            print('Check config.json',e)
        finally:
            self.client=client
            print('Connected to api')
            print("1.Retrieve Data from Binance as Json file\n2.Retrieve Dara from Binance as Json file and Excel file") 
            choice=int(input())
            print('write symbol:')
            sym=input()
            trades = client.get_recent_trades(symbol=sym)
            print("Save as a json file.You have to write file name which you want to save candlestick datas into e.g example.json")
            file=input()
            jf=file
            with open(file,'w') as r:
                file=json.dump(trades,r)
                r.close()
            if choice==1:
                print(trades)
            else:
                with open(jf) as jsonfile:
                    f=json.load(jsonfile)
                    jsonfile.close()
                nj=pd.json_normalize(f)
                print(nj)
                nj.to_excel(sym+'.xlsx')
                
