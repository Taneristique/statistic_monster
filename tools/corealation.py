import tools.covariance as cov
import tools.std as std
import matplotlib.pyplot as plt
import numpy as np
class core:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def pearson(self):
        "Sample must have two relational parameters to have corelation which are x and y arrays or lists for this function"
        r=cov.covariance(self.x,self.y)/(std(self.x)*std(self.y))
        print('r = ', r)
    
    def draw_pearson(self):
        if(len(self.x)==len(self.y)):
            r=cov.covariance(self.x,self.y)/(std(self.x)*std(self.y))
            p=len(self.x)
            a=0
            ym=0
            xm=0
            reg=[]
            ssx=0
            sp=0
            for i in range(p):
                ym+=self.y[i]/len(self.x)
                xm+=self.x[i]/len(self.x)
            for i in range(p):
                 ssx+=(self.x[i]-xm)**2
                 sp+=(self.x[i]-xm)*(self.y[i]-ym)
            b=sp/ssx
            a=ym-b*xm
            for j in range(p):
                reg.append(b*self.x[j]+a)
           
            print("mean(x) is" + str(xm))
            print("mean(y) is" + str(ym))
            print('b is'+ str(b))
            print('a is'+ str(a))
            et=0
            for i in range(len(self.x)):
                et+=(self.y[i]-reg[i])**2/len(self.x)
                print(et)
                print('reg is ',reg[i])
            print('sp is',sp)
            print('ssx is',ssx)
            i=a        # intercept
            s=b        # slope
            if(reg[0]>reg[len(self.x)-1]):
                x=np.linspace(0-self.x[0]-min(reg),max(reg)+max(self.x),100)
            else:
                x=np.linspace(max(reg),0-self.x[0]-min(reg),100)
          
            plt.plot(x, s*x + i)        # abline
            plt.title('r='+str(r))
            plt.xticks(self.x)
            plt.yticks(self.y)
            plt.scatter(self.x,self.y)
            plt.show()          
        else:
            print("Lengths must be equal!")
            

    