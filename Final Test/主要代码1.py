from random import choice
import matplotlib.pyplot as plt
from random import random
import numpy as np
import pandas as pd
from pandas import Series
from sklearn import linear_model
from scipy import optimize
from random import uniform

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


class randomwalk1():
    def __init__(self,u1,num_points1=500):
        self.num_points1=num_points1
        self.x1=[0]
        self.n1=[0]
        self.u1=u1
    def coffee1(self):
        for j1 in range(self.num_points1):
           
            num1=random()
            if num1 < 0.5:
                x1_step=uniform(0,1)
            else :
                x1_step=uniform(-1,0)
            new_x1=self.x1[-1]+x1_step
            self.x1.append(new_x1)
            new_n1=self.n1[-1]+1
            self.n1.append(new_n1)
    
u1=list(range(0,5000))
W1=[]
for i1 in u1:
    k1=randomwalk1(u1[i],500)
    k1.coffee1()
    N1=k1.n1
    X1=k1.x1
    new_X1=[value**2 for value in X1]
    W1.append(new_X1)
M1=np.mean(W1,axis=0)
s1=Series(M1,index=N1)
regr = linear_model.LinearRegression() 
regr.fit(M1.reshape(-1,1),N1)
a1, b1 = regr.coef_, regr.intercept_ 
print(1/a1)
def f_11(x1, A1, B1):  
    return A1*x1 + B1 


A11, B11 = optimize.curve_fit(f_11, N1, M1)[0]  
x11 = np.arange(0, 500, 0.1)  
y11 = A11*x11 + B11 

class randomwalk3():
    def __init__(self,u3,num_points3=500):
        self.num_points3=num_points3
        self.x3=[0]
        self.n3=[0]
        self.u3=u3
    def coffee3(self):
        for j3 in range(self.num_points3):
           
            num3=random()
            if num3 < 0.5:
                x3_step=uniform(0,2)
            else :
                x3_step=uniform(-2,0)
            new_x3=self.x3[-1]+x3_step
            self.x3.append(new_x3)
            new_n3=self.n3[-1]+1
            self.n3.append(new_n3)
    
u3=list(range(0,5000))
W3=[]
for i3 in u3:
    k3=randomwalk3(u3[i],500)
    k3.coffee3()
    N3=k3.n3
    X3=k3.x3
    new_X3=[value**2 for value in X3]
    W3.append(new_X3)
M3=np.mean(W3,axis=0)
s3=Series(M3,index=N3)
regr = linear_model.LinearRegression() 
regr.fit(M3.reshape(-1,1),N3)
a3, b3 = regr.coef_, regr.intercept_ 
print(1/a3)
def f_13(x3, A3, B3):  
    return A3*x3 + B3 

A13, B13 = optimize.curve_fit(f_13, N3, M3)[0]  
x13 = np.arange(0, 500, 0.1)  
y13 = A13*x13 + B13
   
plt.figure(figsize=(10, 6))
plt.scatter(N,M,s=1,color='blue')
plt.scatter(N1,M1,s=1,color='green')
plt.scatter(N3,M3,s=1,color='gray')

plt.plot(x1, y1, color="red",label='MSD for certain step lengths') 
plt.plot(x11,y11,color='black',label='MSD for random step lengths  0<steps<1')
plt.plot(x13,y13,color='purple',label='MSD for random step lengths  0<steps<2')

plt.title('Mean squared displacement in 1D',fontsize=24)
plt.xlabel('step number(=time)',fontsize=14)
plt.ylabel('MSD')
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.legend(loc='upper left')
plt.show()