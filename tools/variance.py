import matplotlib.pyplot as plt

class variance:
    def __init__(self,x,y=None):
        """x and y are sample values,as input only list and array object types are accepted.The y parameter is optional use it if x is subset of y series and len(y) is bigger than len(x)"""
        self.x=x
        self.total=0
        self.sample=len(x)
        self.y=y
        self.ploty=[]
        self.plotx=[]
        for i in range(self.sample):
            self.total+=self.x[i]
        self.avarage=self.total/self.sample
    def calculate_variance(self):
        var=0
        for i in range(self.sample):
            var+=(self.x[i]-self.avarage)**2/self.sample
        return var
    def draw_variance(self):
        var=0
        for i in range(self.sample):
            var+=(self.x[i]-self.avarage)**2/self.sample
            self.ploty.append(var)
            self.plotx.append(self.x[i])
        plt.xlabel('datas')
        plt.ylabel('variance')
        plt.plot(self.plotx,self.ploty,'r--', label='variance')
        plt.plot(self.plotx,self.plotx,'b',color='green',label='data')
        plt.legend(loc='upper left')
        plt.show()
   