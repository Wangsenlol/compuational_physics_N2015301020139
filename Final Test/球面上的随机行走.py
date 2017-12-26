from random import choice
from random import uniform
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from random import random


class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.phi_values=[0]
        self.theta_values=[0]
        self.x=[0]
        self.y=[0]
        self.z=[10]
        
        
        
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
            self.phi_values.append(next_phi) 
            self.theta_values.append(next_theta)
            self.x.append(new_x)
            self.y.append(new_y)
            self.z.append(new_z)
            
rw = RandomWalk(5000) 
rw.fill_walk() 
fig = plt.figure(figsize=(10,6))
ax = fig.gca(projection='3d')

point_numbers=list(range(rw.num_points))
ax.scatter(rw.x, rw.y, rw.z,color='purple',s=3)
ax.scatter(0, 0,10, c='green', edgecolors='none', s=200) 
ax.scatter(rw.x[-1], rw.y[-1],rw.z[-1], c='black', edgecolors='none', s=100) 

plt.title('Random walk in spherical surface',fontsize=24)
ax.set_xlabel("X ",fontsize=20)
ax.set_ylabel("Y ",fontsize=20)
ax.set_zlabel("Z ",fontsize=20)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_zlim(-10,10)
plt.tick_params(axis='both', which='major') 


plt.show()
 