from random import choice
from random import uniform
import matplotlib.pyplot as plt 

class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
        self.x1_values=[0]
        self.y1_values=[0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points: 
            x_direction = choice([1, -1]) 
            x_distance = uniform(0,2)
            x_step = x_direction * x_distance 
            y_direction = choice([1, -1]) 
            y_distance =  uniform(0,2)
            y_step = y_direction * y_distance 
            if x_step == 0 and y_step == 0: 
                continue 
            next_x = self.x_values[-1] + x_step 
            next_y = self.y_values[-1] + y_step 
 
            self.x_values.append(next_x) 
            self.y_values.append(next_y) 
            
    
        while len(self.x1_values) < self.num_points: 
            x1_direction = choice([1, -1]) 
            x1_distance = uniform(0,2)
            x1_step = x1_direction * x1_distance 
            y1_direction = choice([1, -1]) 
            y1_distance =  uniform(0,2)
            y1_step = y1_direction * y1_distance 
            if x1_step == 0 and y1_step == 0: 
                continue 
            next_x1 = self.x1_values[-1] + x1_step 
            next_y1 = self.y1_values[-1] + y1_step 
 
            self.x1_values.append(next_x1) 
            self.y1_values.append(next_y1) 
            
rw = RandomWalk() 
rw.fill_walk() 
plt.figure(figsize=(10, 6)) 
point_numbers=list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
            edgecolor='none',s=3)
plt.scatter(rw.x1_values,rw.y1_values,c=point_numbers,cmap=plt.cm.Reds,
            edgecolor='none',s=3)
plt.scatter(0, 0, c='green', edgecolors='none', s=100) 
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black', edgecolors='none', 
            s=100) 
plt.scatter(rw.x1_values[-1], rw.y1_values[-1], c='yellow', edgecolors='none', 
            s=100) 
 

plt.title('Random walk in 2D for random step lengths',fontsize=24)
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.axes().get_xaxis().set_visible(False) 
plt.axes().get_yaxis().set_visible(False) 
 
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.show()
 
