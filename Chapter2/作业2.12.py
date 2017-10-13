import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

x_1=[]
v1_1=[]
y_1=[]
v2_1=[]
z_1=[]
v3_1=[]

x_2=[]
v1_2=[]
y_2=[]
v2_2=[]
z_2=[]
v3_2=[]

x_3=[]
v1_3=[]
y_3=[]
v2_3=[]
z_3=[]
v3_3=[]

x_4=[]
v1_4=[]
y_4=[]
v2_4=[]
z_4=[]
v3_4=[]
t=[]
v=0.7
w=2*np.pi/(24*3600)
B2=4*10**-2
m=1
T_0=300
a=6.5
alpha=2.5
g=9.8*10**-3
det_t=0.1
x_1.append(0)
y_1.append(0)
z_1.append(0)

x_2.append(0)
y_2.append(0)
z_2.append(0)

x_3.append(0)
y_3.append(0)
z_3.append(0)

x_4.append(0)
y_4.append(0)
z_4.append(0)
t.append(0)
n=list(range(0,1000))
v1_1.append(v*np.cos(np.pi/6))
v2_1.append(0)
v3_1.append(v*np.sin(np.pi/6))

v1_2.append(v*np.cos(np.pi/4))
v2_2.append(0)
v3_2.append(v*np.sin(np.pi/4))

v1_3.append(v*np.cos(np.pi/3))
v2_3.append(0)
v3_3.append(v*np.sin(np.pi/3))

v1_4.append(v*np.cos(np.pi*5/12))
v2_4.append(0)
v3_4.append(v*np.sin(np.pi*5/12))

for i in n:
      X_1=x_1[i]+v1_1[i]*det_t
      u1_1=v1_1[i]-(2*w*v2_1[i]+(B2*v*v1_1[i]/m)*(1-a*z_1[i]/T_0)**alpha)*det_t
      x_1.append(X_1)
      v1_1.append(u1_1)
      Y_1=y_1[i]+v2_1[i]*det_t
      u2_1=v2_1[i]+(2*w*v1_1[i]-(B2*v*v2_1[i]/m)*(1-a*z_1[i]/T_0)**alpha)*det_t
      y_1.append(Y_1)
      v2_1.append(u2_1)
      Z_1=z_1[i]+v3_1[i]*det_t
      u3_1=v3_1[i]-(g+(B2*v*v3_1[i]/m)*(1-a*z_1[i]/T_0)**alpha)*det_t
      z_1.append(Z_1)
      v3_1.append(u3_1)
      
      X_2=x_2[i]+v1_2[i]*det_t
      u1_2=v1_2[i]-(2*w*v2_2[i]+(B2*v*v1_2[i]/m)*(1-a*z_2[i]/T_0)**alpha)*det_t
      x_2.append(X_2)
      v1_2.append(u1_2)
      Y_2=y_2[i]+v2_2[i]*det_t
      u2_2=v2_2[i]+(2*w*v1_2[i]-(B2*v*v2_2[i]/m)*(1-a*z_2[i]/T_0)**alpha)*det_t
      y_2.append(Y_2)
      v2_2.append(u2_2)
      Z_2=z_2[i]+v3_2[i]*det_t
      u3_2=v3_2[i]-(g+(B2*v*v3_2[i]/m)*(1-a*z_2[i]/T_0)**alpha)*det_t
      z_2.append(Z_2)
      v3_2.append(u3_2)
      
      X_3=x_3[i]+v1_3[i]*det_t
      u1_3=v1_3[i]-(2*w*v2_3[i]+(B2*v*v1_3[i]/m)*(1-a*z_3[i]/T_0)**alpha)*det_t
      x_3.append(X_3)
      v1_3.append(u1_3)
      Y_3=y_3[i]+v2_3[i]*det_t
      u2_3=v2_3[i]+(2*w*v1_3[i]-(B2*v*v2_3[i]/m)*(1-a*z_3[i]/T_0)**alpha)*det_t
      y_3.append(Y_3)
      v2_3.append(u2_3)
      Z_3=z_3[i]+v3_3[i]*det_t
      u3_3=v3_3[i]-(g+(B2*v*v3_3[i]/m)*(1-a*z_3[i]/T_0)**alpha)*det_t
      z_3.append(Z_3)
      v3_3.append(u3_3)
      
      X_4=x_4[i]+v1_4[i]*det_t
      u1_4=v1_4[i]-(2*w*v2_4[i]+(B2*v*v1_4[i]/m)*(1-a*z_4[i]/T_0)**alpha)*det_t
      x_4.append(X_4)
      v1_4.append(u1_4)
      Y_4=y_4[i]+v2_4[i]*det_t
      u2_4=v2_4[i]+(2*w*v1_4[i]-(B2*v*v2_4[i]/m)*(1-a*z_4[i]/T_0)**alpha)*det_t
      y_4.append(Y_4)
      v2_4.append(u2_4)
      Z_4=z_4[i]+v3_4[i]*det_t
      u3_4=v3_4[i]-(g+(B2*v*v3_4[i]/m)*(1-a*z_4[i]/T_0)**alpha)*det_t
      z_4.append(Z_4)
      v3_4.append(u3_4)
      t.append(det_t*(i+1))
      if z_1[-1]>=0:
          print(x_1[-1],y_1[-1],z_1[-1])
      if z_2[-1]>=0:
          print(x_2[-1],y_2[-1],z_2[-1])
      if z_3[-1]>=0:
          print(x_3[-1],y_3[-1],z_3[-1])
      if z_4[-1]>=0:
          print(x_4[-1],y_4[-1],z_4[-1])

plt.title('Trajectory of cannon shell with Coriolis force',fontsize=14)
line1=ax.plot(x_1,y_1,z_1,color='blue',label='$\phi=\pi/6$')
line2=ax.plot(x_2,y_2,z_2,color='red',label='$\phi=\pi/4$')
line3=ax.plot(x_3,y_3,z_3,color='yellow',label='$\phi=\pi/3$')
line4=ax.plot(x_4,y_4,z_4,color='black',label='$\phi=5\pi/12$')
plt.xlabel('x(km)',fontsize=14)
plt.xlim(0,55)
plt.ylabel('y(km)',fontsize=14)
plt.ylim(0,0.1)
ax.set_zlabel('z(km)',fontsize=14)
ax.set_zlim(0,12)
plt.legend()

plt.show()
    
    

