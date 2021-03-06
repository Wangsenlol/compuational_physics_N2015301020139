import matplotlib.pyplot as plt
import numpy as np

r_m=[]
r_j=[]
r_mj=[]
v_mx=[0]
v_my=[5.08]
v_jx=[0]
v_jy=[2.74]
x_m=[1.52]
y_m=[0]
x_j=[5.2]
y_j=[0]
a=0.001
b=3.3*10**(-6)
dt=0.001
n=list(range(0,15000))
for i in n:
    new_r_m=np.sqrt(x_m[-1]**2+y_m[-1]**2)
    new_r_j=np.sqrt(x_j[-1]**2+y_j[-1]**2)
    new_r_mj=np.sqrt((x_m[-1]-x_j[-1])**2+(y_m[-1]-y_j[-1])**2)
    r_m.append(new_r_m)
    r_j.append(new_r_j)
    r_mj.append(new_r_mj)
    new_v_mx=v_mx[-1]-(4*(np.pi)**2*x_m[-1]/(r_m[-1])**3)*dt-(4*(np.pi)**2*a*(x_m[-1]-x_j[-1])/(r_mj[-1])**3)*dt
    new_v_my=v_my[-1]-(4*(np.pi)**2*y_m[-1]/(r_m[-1])**3)*dt-(4*(np.pi)**2*a*(y_m[-1]-y_j[-1])/(r_mj[-1])**3)*dt
    new_v_jx=v_jx[-1]-(4*(np.pi)**2*x_j[-1]/(r_j[-1])**3)*dt-(4*(np.pi)**2*b*(x_j[-1]-x_m[-1])/(r_mj[-1])**3)*dt
    new_v_jy=v_jy[-1]-(4*(np.pi)**2*y_j[-1]/(r_j[-1])**3)*dt-(4*(np.pi)**2*b*(y_j[-1]-y_m[-1])/(r_mj[-1])**3)*dt
    v_mx.append(new_v_mx)
    v_my.append(new_v_my)
    v_jx.append(new_v_jx)
    v_jy.append(new_v_jy)
    new_x_m=x_m[-1]+v_mx[-1]*dt
    new_y_m=y_m[-1]+v_my[-1]*dt
    new_x_j=x_j[-1]+v_jx[-1]*dt
    new_y_j=y_j[-1]+v_jy[-1]*dt
    x_m.append(new_x_m)
    y_m.append(new_y_m)
    x_j.append(new_x_j)
    y_j.append(new_y_j)
    
plt.figure(figsize=(8,8))
plt.title('3-body simulation  Mars plus Jupiter  Mass of Jupiter=$M_J$')
plt.plot(x_m,y_m,color='red',label='Mars')
plt.plot(x_j,y_j,color='blue',label='Jupiter')
plt.xlabel('x(AU)',fontsize=16)
plt.ylabel('y(AU)',fontsize=16)
plt.legend(loc='best')
plt.show()