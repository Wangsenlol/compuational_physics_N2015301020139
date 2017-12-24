from random import choice
import matplotlib.pyplot as plt
from random import uniform

class randomwalk():
    def __init__(self,num_points=500):
        self.num_points=num_points
        self.x_1=[0]
        self.x_2=[0]
        self.x_3=[0]
        self.x_4=[0]
        self.n_1=[0]
        self.n_2=[0]
        self.n_3=[0]
        self.n_4=[0]
        
    def coffee(self):
        while len(self.n_1) < self.num_points:
            num=uniform(0,1)
            if num < 0.5:
                x_1_step=1
            else:
                x_1_step=-1
            
            new_x_1=self.x_1[-1]+x_1_step
            new_n_1=self.n_1[-1]+1
            self.x_1.append(new_x_1)
            self.n_1.append(new_n_1)
            
        while len(self.n_2) < self.num_points:
            num=uniform(0,1)
            if num < 0.5:
                x_2_step=1
            else:
                x_2_step=-1
           
            new_x_2=self.x_2[-1]+x_2_step
            new_n_2=self.n_2[-1]+1
            self.x_2.append(new_x_2)
            self.n_2.append(new_n_2)
            
        while len(self.n_3) < self.num_points:
            num=uniform(0,1)
            if num < 0.5:
                x_3_step=1
            else:
                x_3_step=-1
          
            new_x_3=self.x_3[-1]+x_3_step
            new_n_3=self.n_3[-1]+1
            self.x_3.append(new_x_3)
            self.n_3.append(new_n_3)
            
        while len(self.n_4) < self.num_points:
            num=uniform(0,1)
            if num < 0.5:
                x_4_step=1
            else:
                x_4_step=-1
         
            new_x_4=self.x_4[-1]+x_4_step
            new_n_4=self.n_4[-1]+1
            self.x_4.append(new_x_4)
            self.n_4.append(new_n_4)
      
      
            
rw=randomwalk()
rw.coffee()
plt.figure(figsize=(10, 6)) 
point_numbers=list(range(rw.num_points))

plt.scatter(rw.n_1,rw.x_1,c=point_numbers,cmap=plt.cm.Blues,
            edgecolor='none',s=10)
plt.scatter(rw.n_2,rw.x_2,c=point_numbers,cmap=plt.cm.Reds,
            edgecolor='none',s=10)
plt.scatter(rw.n_3,rw.x_3,c=point_numbers,cmap=plt.cm.Greens,
            edgecolor='none',s=10)
plt.scatter(rw.n_4,rw.x_4,c=point_numbers,cmap=plt.cm.Purples,
            edgecolor='none',s=10)

plt.title('Random walk in 1D for certain step lengths',fontsize=24)
plt.xlabel('step number=(time)',fontsize=14)
plt.ylabel('x',fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14) 
plt.show()
