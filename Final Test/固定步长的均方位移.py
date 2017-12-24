from random import choice
import matplotlib.pyplot as plt
from random import random
import numpy as np
from random import uniform
import pandas as pd
from pandas import Series
from sklearn import linear_model
from scipy import optimize

class randomwalk():
    def __init__(self,u,num_points=500):
        self.num_points=num_points
        self.x=[0]
        self.n=[0]
        self.u=u
    def coffee(self):
        for j in range(self.num_points):
           
            num=random()
            if num < 0.5:
                x_step=1
            else :
                x_step=-1
            new_x=self.x[-1]+x_step
            self.x.append(new_x)
            new_n=self.n[-1]+1
            self.n.append(new_n)
    
u=list(range(0,5000))
W=[]
for i in u:
    k=randomwalk(u[i],500)
    k.coffee()
    N=k.n
    X=k.x
    new_X=[value**2 for value in X]
    W.append(new_X)
M=np.mean(W,axis=0)
s=Series(M,index=N)
regr = linear_model.LinearRegression() 
regr.fit(M.reshape(-1,1),N)
a, b = regr.coef_, regr.intercept_ 
print(1/a)
def f_1(x, A, B):  
    return A*x + B  

A1, B1 = optimize.curve_fit(f_1, N, M)[0]  
x1 = np.arange(0, 500, 0.1)  
y1 = A1*x1 + B1  
   


 
plt.figure(figsize=(10, 6))
plt.scatter(N,M,s=1)
plt.plot(x1, y1, color="red",label='MSD for certain step lengths') 
plt.title('Mean squared displacement in 1D',fontsize=24)
plt.xlabel('step number(=time)',fontsize=14)
plt.ylabel('MSD')
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.legend(loc='upper left')
plt.show()