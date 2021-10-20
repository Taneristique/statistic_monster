import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
from sklearn.metrics import r2_score
import numpy as np
def calc_interest():
    main_amount=int(input('How much money you have?\n'))
    rate=float(input('interest rate as float e.g 0.06:\n'))
    period_n=int(input('How many years will you put your money to normal interest? e.g 100 for one hundred years\n'))
    period=1
    gain_x_month=int(input("In which frequence the compound interest will be paid to you?\nfor example if period 1 and frequence 2 it means every 6 months compound interest will be paid in a year.\n"))
    print('please chose repeating at least 5')    
    repeat=int(input('How many times repeat compound interest?\n you will increase the year you hold your money in compound interest if repeating value is more than 1\nand do not forget float value is not allowed,only integer values accepted!\n'))
    normal_interest_gains=[]
    normal_interest_time=[]
    def normal_interest(initial_capital,rate,length):
        for i in range(length):
            normal_interest_time.append(i+1)
            initial_capital*=pow((1+rate),(i+1))
            normal_interest_gains.append(initial_capital)
            print( 'year : ', normal_interest_time[i], 'normal interest gains :', normal_interest_gains[i])
            
    normal_interest(main_amount,rate,period_n)

    compound_interest_gains=[]
    year_register=[]
    tp=[]

    def compound_interest(initial_amount,rate,month_length,gain_per_n_month):
        count=1
        count_empty_time=0
        interest_gaining_time=month_length/gain_per_n_month
        compound_interest_gains.append(initial_amount*pow((1+rate/interest_gaining_time),interest_gaining_time))
        year=month_length/12
        year_register.append(year)
        
    def run_compound_interest(initial_amount,rate,month_length,gain_per_n_month,repeat):
        c=[]
        last_capital=0
        for i in range(repeat): 
            i+=1
            compound_interest(initial_amount,rate,month_length*i,gain_per_n_month)
            last_capital+=compound_interest_gains[i-1]
            tp.append(last_capital-initial_amount)
            print( 'year : ', year_register[i-1], 'compound interest gains :', compound_interest_gains[i-1])
            
        return 'total profit : ',last_capital-initial_amount
    period_as_month=period=12*period
    run_compound_interest(main_amount,rate,period_as_month,gain_x_month,repeat)

    plt.figure(figsize=(12,4))
    plt.plot(compound_interest_gains,tp)
    plt.show()

    plt.figure(figsize=(12,4))
    plt.plot(compound_interest_gains)
    plt.xticks(year_register)
    plt.show()

    model=linear_model.LinearRegression()
    x0=np.array(year_register).reshape(-1,1)
    y0=np.array(compound_interest_gains)
    model.fit(x0,y0)
    r_sq=model.score(x0,y0)

    print('coefficient of determination r**2 is ',r_sq)

    yfit = model.predict(x0)
    plt.figure(figsize=(16,9))
    plt.scatter(x0, y0)
    plt.plot(x0, yfit);
    plt.legend(['compound_interest_gains','regression_line'])
    plt.show()

    model2=linear_model.LinearRegression()
    x=np.array(normal_interest_time).reshape(-1,1)
    y=np.array(normal_interest_gains)
    model2.fit(x,y)
    r_sq = model.score(x, y)
    print('coefficient of determination r**2 is ',r_sq)
    yfit=model2.predict(x)
    plt.figure(figsize=(16,9))
    plt.scatter(x,y)
    plt.plot(x,yfit)
    plt.legend(['normal_interest_gains','regression_line'])
    plt.show()
