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
        self.phi_values=[0]
        self.theta_values=[0]
        self.x=[0]
        self.y=[0]
        self.z=[10]
        self.u=u
        self.n=[0]
        self.r=[0]
        
        
        
    def fill_walk(self):
        for j in range(self.num_points):
            num1=random()
            if num1 < 0.5:
                phi_direction =1
            else:
                phi_direction=-1
            phi_distance = uniform(0,np.pi/18)
            phi_step = phi_direction * phi_distance 
            num2=random()
            if num2 < 0.5:
                theta_direction=1
            else:
                theta_direction=-1
            theta_distance =  uniform(0,np.pi/18)
            theta_step = theta_direction * theta_distance 
            next_phi = self.phi_values[-1] + phi_step 
            next_theta = self.theta_values[-1] + theta_step 
            new_x=10*np.sin(next_theta)*np.cos(next_phi)
            new_y=10*np.sin(next_theta)*np.sin(next_phi)
            new_z=10*np.cos(next_theta)
            new_r=np.sqrt(new_x**2+new_y**2+(new_z-10)**2)
            self.phi_values.append(next_phi) 
            self.theta_values.append(next_theta)
            self.x.append(new_x)
            self.y.append(new_y)
            self.z.append(new_z)
            self.r.append(new_r)
            new_n=self.n[-1]+1
            self.n.append(new_n)
            


u=list(range(0,5000))
W=[]
for i in u:
    k=RandomWalk(u[i],50)
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
x1 = np.arange(0, 50, 0.1)  
y1 = A1*x1 + B1  

plt.figure(figsize=(10, 6))
plt.scatter(N,M,s=1,color='blue')



plt.plot(x1,y1,color='purple')

plt.title('Mean squared displacement in spherical surface',fontsize=24)
plt.xlabel('step number(=time)',fontsize=14)
plt.ylabel('MSD')
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.show()