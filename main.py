import json
import numpy as np
import pandas as pd
from tools import *
import pyfiglet
result = pyfiglet.figlet_format("STATISTIC MONSTER\nDesigned By  Taneristique\nv1.0", font = "rectangles"  )
print(result)

def covariance():
    print('1.CALCULATE FROM JSON DATA\n2.CALCULATE COVARIANCE MANUALLY\n3.DRAW FROM JSON DATA\n4.GIVE MANUAL DATA FOR TWO COVARIANCE PARAMETERS THAN DRAW')
    chose=int(input(''))
    if(chose==1):
        print('write file name e.g example.json')
        
        file=input()

        try:
            with open(file) as f:
                file=json.load(f)
                f.close()
        except Exception as a:
            print(a)            
        finally:
            n=pd.json_normalize(file)
            print(n)
            print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
            length=int(input())
            print('please write the name of the column e.g price')
            name=input()
            answer=[]
            for i in range(length):
                answer.append(float(file[i].get(name)))
            print('we will reply the same operation for y parameter but before continuing please write y if you want another json file for y parameter else write n!')
            write=input()
            if(write=='y'):
                print('write file name e.g example.json')
                filet=input()
                try:
                    with open(filet) as f:
                        filet=json.load(f)
                        f.close()
                except Exception as a:
                     print(a)           
                finally:
                    n=pd.json_normalize(filet)
                    print(n)
                    print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
                    print('please write the name of the column e.g price')
                    n=input()
                    ao=[]
                    for i in range(length):
                        ao.append(float(file[i].get(name)))
                    print('Covariance calculated!\n')
                    print(cov.covariance(answer,ao))
            else:
                name=[]
                print('please write the name of the column e.g price')
                name=input()
                ao=[]
                for i in range(length):
                    ao.append(float(file[i].get(name)))
                print('Covariance calculated!\n')
                print(cov.covariance(answer,ao))
    elif(chose==2):
        print('Length of datasets?')
        length=int(input())
        x=[]
        y=[]
        v=0
        print("Please give first dataset's values!")
        for i in range(length):
            print('x[',i,']:')
            v=float(input())
            x.append(v)
            print('\n')
        print("Please give second dataset's values!")
        for i in range(length):
            print('y[',i,']:')
            v=float(input())
            y.append(v)
            print('\n')
        print('Covariance calculated!')
        print(cov.covariance(x,y))
    elif(chose==3):
        print('write file name e.g example.json')
        
        file=input()

        try:
            with open(file) as f:
                file=json.load(f)
                f.close()
        except Exception as a:
            print(a)            
        finally:
            n=pd.json_normalize(file)
            print(n)
            print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
            length=int(input())
            print('please write the name of the column e.g price')
            name=input()
            answer=[]
            for i in range(length):
                answer.append(float(file[i].get(name)))
            print('we will reply the same operation for y parameter but before continuing please write y if you want another json file for y parameter else write n!')
            write=input()
            if(write=='y'):
                print('write file name e.g example.json')
                filet=input()
                try:
                    with open(filet) as f:
                        filet=json.load(f)
                        f.close()
                except Exception as a:
                     print(a)           
                finally:
                    n=pd.json_normalize(filet)
                    print(n)
                    print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
                    print('please write the name of the column e.g price')
                    n=input()
                    ao=[]
                    for i in range(length):
                        ao.append(float(file[i].get(name)))
                    print('Covariance calculated!\n')
                    print(cov.draw_cov(answer,ao))
            else:
                name=[]
                print('please write the name of the column e.g price')
                name=input()
                ao=[]
                for i in range(length):
                    ao.append(float(file[i].get(name)))
                print(cov.draw_cov(answer,ao))
    elif(chose==4):
        print('Length of datasets?')
        length=int(input())
        x=[]
        y=[]
        v=0
        print("Please give first dataset's values!")
        for i in range(length):
            print('x[',i,']:')
            v=float(input())
            x.append(v)
            print('\n')
        print("Please give second dataset's values!")
        for i in range(length):
            print('y[',i,']:')
            v=float(input())
            y.append(v)
            print('\n')
        print(cov.draw_cov(x,y))


def variance():
    print('1.VARIANCE OF A JSON DATASET\n2.FIND VARIANCE OF A MANUAL DATASET')
    chose=int(input())
    if(chose==1):
        print('write file name e.g example.json')
        
        file=input()

        try:
            with open(file) as f:
                file=json.load(f)
                f.close()
        except Exception as a:
            print(a)            
        finally:
            n=pd.json_normalize(file)
            print(n)
            print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
            length=int(input())
            print('please write the name of the column e.g price')
            name=input()
            answer=[]
            for i in range(length):
                answer.append(float(file[i].get(name)))
            print('Variance is', var(answer).calculate_variance())
            print("Would you want to draw its' graphic if yes write y")
            a=input()
            if a=='y':
                var(answer).draw_variance()
    if(chose==2):
        print('Length of dataset?')
        length=int(input())
        x=[]
        v=0
        print("Please give first dataset's values!")
        for i in range(length):
            print('x[',i,']:')
            v=float(input())
            x.append(v)
            print('\n')
        print('Variance is',var(x).calculate_variance()) 
        print("Would you want to draw its' graphic if yes write y")
        a=input()
        if a=='y':
            var(x).draw_variance()       
def standard_deviation():
    print('1.FIND STANDARD DEVIATION OF A JSON DATASET\n2.FIND STANDARD DEVIATION OF A MANUAL DATASET')
    chose=int(input())
    if(chose==1):
        print('write file name e.g example.json')
        
        file=input()

        try:
            with open(file) as f:
                file=json.load(f)
                f.close()
        except Exception as a:
            print(a)            
        finally:
            n=pd.json_normalize(file)
            print(n)
            print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
            length=int(input())
            print('please write the name of the column e.g price')
            name=input()
            answer=[]
            for i in range(length):
                answer.append(float(file[i].get(name)))
            print('standard deviation is', std(answer))
    if(chose==2):
        print('Length of dataset?')
        length=int(input())
        x=[]
        v=0
        print("Please give a dataset!")
        for i in range(length):
            print('x[',i,']:')
            v=float(input())
            x.append(v)
            print('\n')
        print('standard deviation is', std(answer))
def corelation():
    print('1.GET DATASETS FROM JSON\n2.WRITE DATASET MANUALLY')
    chose=int(input())
    if(chose==1):
        print('write file name e.g example.json')
        
        file=input()

        try:
            with open(file) as f:
                file=json.load(f)
                f.close()
        except Exception as a:
            print(a)            
        finally:
            n=pd.json_normalize(file)
            print(n)
            print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
            length=int(input())
            print('please write the name of the column e.g price')
            name=input()
            answer=[]
            for i in range(length):
                answer.append(float(file[i].get(name)))
            print('we will reply the same operation for y parameter but before continuing please write y if you want another json file for y parameter else write n!')
            write=input()
            if(write=='y'):
                print('write file name e.g example.json')
                filet=input()
                try:
                    with open(filet) as f:
                        filet=json.load(f)
                        f.close()
                except Exception as a:
                     print(a)           
                finally:
                    n=pd.json_normalize(filet)
                    print(n)
                    print("The above you will see the values each row means a list and first row's index is 0.Please write how many rows you want to retrieve!")
                    print('please write the name of the column e.g price')
                    n=input()
                    ao=[]
                    for i in range(length):
                        ao.append(float(file[i].get(name)))
                    print('Correlation calculated!\n')
                    print(core(answer,ao).pearson())
                    print("Would you want to draw its' graphic if yes write y")
                    a=input()
                    if a=='y':
                        core(answer,ao).draw_pearson()
            else:
                name=[]
                print('please write the name of the column e.g price')
                name=input()
                ao=[]
                for i in range(length):
                    ao.append(float(file[i].get(name)))
                print('Correlation calculated!\n')
                print(core(answer,ao).pearson())
                print("Would you want to draw its' graphic if yes write y")
                a=input()
                if a=='y':
                    core(answer,ao).draw_pearson()
    if(chose==2):
        print('Length of dataset?')
        length=int(input())
        x=[]
        y=[]
        v=0
        print("Please give a dataset!")
        for i in range(length):
            print('x[',i,']:')
            v=float(input())
            x.append(v)
            print('\n')
        for i in range(length):
            print('x[',i,']:')
            v=float(input())
            y.append(v)
            print('\n')
        core(x,y).pearson()
        print("Would you want to draw its' graphic if yes write y")

        a=input()
        if a=='y':
            core(x,y).draw_pearson()  
def connect_binance():
    connection()

def menu():
    print("1.DRAW OR CALCULATE COVARIANCE\n2.DRAW OR CALCULATE VARIANCE\n3.CALCULATE STANDART DEVIATION\n4.CALCULATE CORELATION\n5.GET DATA FROM BINANCE")
    chose=int(input())

    options={1 : covariance,
             2 : variance,
             3 : standard_deviation,
             4 : corelation,
             5 : connect_binance
    }
    options[chose]()
if __name__ == "__main__":
    menu()
    
