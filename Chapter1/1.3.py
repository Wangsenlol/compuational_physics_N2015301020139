import numpy as np  #to import matplotlib's package
import matplotlib.pyplot as plt
x1=[]
y1=[]
a=10                 #assign a value to a
b=1                  #assign a value to b
det_x1=0.1           #time step
x1.append(0)         #assign a value to first item of x1[]
y1.append(0)         #assign a value to first item of y1[]
n=list(range(0,100))
x2=np.linspace(0,10,1000)  
y2=10-10*np.exp(-x2)    

for i in n:
    u=y1[i]+(a-b*y1[i])*det_x1   #Euler method
    y1.append(u)                 #add new value of y1 to y1[]
    x1.append(det_x1*(i+1))      #add new value of x1 to x1[]
    print(y1[-1],x1[-1])         #print the value of y1 and x1 on each step
    
plt.figure(figsize=(8,6))        #set the size of corresponding figure

ax=plt.subplot(111)              #add subplot
plt.title("a=10,b=1",fontsize=24) #set the title of the plot
line1=ax.plot(x1,y1,color="blue",label='Euler Method')
line2=ax.plot(x2,y2,color="red",label='Precise Solution')
plt.xlabel("t(s)",fontsize=14)     #set the label of x axis
plt.ylabel("v(m/s)",fontsize=14)   #set the label of y axis
plt.tick_params(axis='both',labelsize=14)  #set the size of tick_params
plt.legend(loc='upper left')  #make it to show everything
plt.show()  #activite