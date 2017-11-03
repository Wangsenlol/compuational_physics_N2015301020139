import matplotlib.pyplot as plt
import numpy as np

np.sigma=10
b=8/3
r=160
dt=0.0001
x=[]
y=[]
z=[]
t=[]
x.append(1)
y.append(0)
z.append(0)
t.append(0)
n=list(range(0,500000))
for i in n:
    new_x=x[i]+np.sigma*(y[i]-x[i])*dt
    new_y=y[i]+(-x[i]*z[i]+r*x[i]-y[i])*dt
    new_z=z[i]+(x[i]*y[i]-b*z[i])*dt
    x.append(new_x)
    y.append(new_y)
    z.append(new_z)
    t.append(dt*(i+1))
    
plt.plot(t,z)
plt.xlabel('time',fontsize=14)
plt.ylabel('z',fontsize=14)
plt.title('Lorenz model z versus time,r=160',fontsize=24)
plt.show()