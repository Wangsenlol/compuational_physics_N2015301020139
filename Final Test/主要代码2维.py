from random import choice
import matplotlib.pyplot as plt
from random import random
import numpy as np
from random import uniform
import pandas as pd
from pandas import Series
from sklearn import linear_model
from scipy import optimize

class RandomWalk():
    def __init__(self,u,num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
        self.u=u
        self.r=[0]
        self.n=[0]

        
    def fill_walk(self):
        for j in range(self.num_points):
            num1=random()
            if num1 < 0.5:
                x_direction=1
            else:
                x_direction=-1
            x_distance = uniform(0,2)
            x_step = x_direction * x_distance 
            next_x = self.x_values[-1] + x_step 
            num2=random()
            if num2 <0.5:
                y_direction=1
            else:
                y_direction=-1
            y_distance =  uniform(0,2)
            y_step = y_direction * y_distance 
            
            next_y = self.y_values[-1] + y_step 
            next_r=np.sqrt(next_x**2+next_y**2)
            self.x_values.append(next_x) 
            self.y_values.append(next_y) 
            self.r.append(next_r)
            new_n=self.n[-1]+1
            self.n.append(new_n)
            
u=list(range(0,5000))
W=[]
for i in u:
    k=RandomWalk(u[i],500)
    k.fill_walk()  
    N=k.n
    R=k.r
    new_R=[value**2 for value in R]
    W.append(new_R)
    
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
        
class RandomWalk1():
    def __init__(self,u1,num_points1=5000):
        self.num_points1=num_points1
        self.x1_values=[0]
        self.y1_values=[0]
        self.u1=u1
        self.r1=[0]
        self.n1=[0]

        
    def fill_walk1(self):
        for j1 in range(self.num_points1):
            num11=random()
            if num11 < 0.5:
                x1_direction=1
            else:
                x1_direction=-1
            x1_distance = uniform(0,1)
            x1_step = x1_direction * x1_distance 
            next_x1 = self.x1_values[-1] + x1_step 
            num21=random()
            if num21 <0.5:
                y1_direction=1
            else:
                y1_direction=-1
            y1_distance =  uniform(0,1)
            y1_step = y1_direction * y1_distance 
            
            next_y1 = self.y1_values[-1] + y1_step 
            next_r1=np.sqrt(next_x1**2+next_y1**2)
            self.x1_values.append(next_x1) 
            self.y1_values.append(next_y1) 
            self.r1.append(next_r1)
            new_n1=self.n1[-1]+1
            self.n1.append(new_n1)
            
u1=list(range(0,5000))
W1=[]
for i in u:
    k1=RandomWalk1(u1[i],500)
    k1.fill_walk1()  
    N1=k1.n1
    R1=k1.r1
    new_R1=[value**2 for value in R1]
    W1.append(new_R1)
    
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
            

class RandomWalk2():
    def __init__(self,u2,num_points2=5000):
        self.num_points2=num_points2
        self.x2_values=[0]
        self.y2_values=[0]
        self.u2=u2
        self.r2=[0]
        self.n2=[0]

        
    def fill_walk2(self):
        for j2 in range(self.num_points2):
            num12=random()
            if num12 < 0.5:
                x2_direction=1
            else:
                x2_direction=-1
            x2_distance = 1
            x2_step = x2_direction * x2_distance 
            next_x2 = self.x2_values[-1] + x2_step 
            num22=random()
            if num22 <0.5:
                y2_direction=1
            else:
                y2_direction=-1
            y2_distance =  -1
            y2_step = y2_direction * y2_distance 
            
            next_y2 = self.y2_values[-1] + y2_step 
            next_r2=np.sqrt(next_x2**2+next_y2**2)
            self.x2_values.append(next_x2) 
            self.y2_values.append(next_y2) 
            self.r2.append(next_r2)
            new_n2=self.n2[-1]+1
            self.n2.append(new_n2)
            
u2=list(range(0,5000))
W2=[]
for i in u2:
    k2=RandomWalk2(u2[i],500)
    k2.fill_walk2()  
    N2=k2.n2
    R2=k2.r2
    new_R2=[value**2 for value in R2]
    W2.append(new_R2)
    
M2=np.mean(W2,axis=0)
s2=Series(M2,index=N2)
regr = linear_model.LinearRegression() 
regr.fit(M2.reshape(-1,1),N2)
a2, b2 = regr.coef_, regr.intercept_ 
print(1/a2)
def f_12(x2, A2, B2):  
    return A2*x2 + B2  

A12, B12 = optimize.curve_fit(f_12, N2, M2)[0]  
x12 = np.arange(0, 500, 0.1)  
y12 = A12*x12 + B12  



plt.figure(figsize=(10, 6))
plt.scatter(N,M,s=1,color='blue')
plt.scatter(N1,M1,s=1,color='green')
plt.scatter(N2,M2,s=1,color='gray')

plt.plot(x12, y12, color="red",label='MSD for certain step lengths') 
plt.plot(x11,y11,color='black',label='MSD for random step lengths  0<steps<1')
plt.plot(x1,y1,color='purple',label='MSD for random step lengths  0<steps<2')

plt.title('Mean squared displacement in 2D',fontsize=24)
plt.xlabel('step number(=time)',fontsize=14)
plt.ylabel('MSD')
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.legend(loc='upper left')
plt.show()