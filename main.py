
import pyfiglet
from modules import *
result = pyfiglet.figlet_format("STATISTIC MONSTER\nDesigned By  Taneristique\nv1.1", font = "rectangles"  )
print(result)
def z_score_datas():
    z.z__score()
def croquie():
    mq.make_croquie()
def interest():
    intr.calc_interest()
def menu():
    Menu='Menu\n1.Get linear regression,correlation,covariation,candlestick graphic,simple moving avarage,macd,momentum data and live price changes from Binance\n2.Calculate Interest and draw regression graph of interest(normal and compound interest)\n3.Get z-score from binance data' 
    print(Menu)
    chose=int(input())
    action_list={1:croquie,2:interest,3:z_score_datas}
    action_list[chose]()

if __name__ == '__main__':
    menu()
    