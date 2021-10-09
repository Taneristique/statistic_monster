import matplotlib.pyplot as plt
def covariance(x,y):
    """x and y must be list or array object!and len(x) must be equal to len(y)"""
    if(len(x)==len(y)):
        c=0
        c1=0
        cov=0
        p=len(x)
        for i in range(p):
            c+=x[i]/len(x)
            c1=y[i]/len(y)
        for j in range(p):
            cov+=((x[j]-c)*(y[j]-c1))/(len(x))
        return cov
    else:
        print('lengths of series must be equal')
    
def draw_cov(x,y):
    if(len(x)==len(y)):   
        c=0
        c1=0
        cov=0
        cd=[]
        p=len(x)
        for i in range(p):
            c+=x[i]/len(x)
            c1=y[i]/len(y)
        for j in range(p):
            cov+=((x[j]-c)*(y[j]-c1))/(len(x)-1)
            cd.append(cov)

        plt.xlabel("population")
        plt.ylabel("covariance")
        plt.plot(x,'r--',label='x')
        plt.plot(y,'g--',label='y')
        plt.plot(cd,color='black',label='covariance')
        plt.legend(loc='upper right')
        plt.show()
    else:
        print('lengths of series must be equal')
