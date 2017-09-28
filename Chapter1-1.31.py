import numpy as np
import matplotlib.pyplot as plt
x1=[]
y1=[]
a=10
b=1
det_t=0.1
x1.append(0)
y1.append(20)
n=list(range(0,100))
x2=np.linspace(0,10,1000)
y2=10-10*np.exp(-x2)

for i in n:
    u=y1[i]+(a-b*y1[i])*det_t
    y1.append(u)
    x1.append(det_t*(i+1))
    print(y1[-1],x1[-1])
    
plt.figure(figsize=(8,6))

ax=plt.subplot(111)
plt.title("a=10,b=1",fontsize=24)
line1=ax.plot(x1,y1,color="blue",label='Euler Method')
line2=ax.plot(x2,y2,color="red",label='Precise Solution')
plt.xlabel("t(s)",fontsize=14)
plt.ylabel("v(m/s)",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.legend(loc='upper left')
plt.show()