import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

g=9.8
omega=4000*np.pi/60
vd=35
v_wind=3
Delta=5
S0m=0.00041
class baseball:
    def __init__(self,v0,theta,zFinal=0):
        self.x0=0
        self.y0=0
        self.z0=1.8 #考虑击球者的身高
        self.zFinal=zFinal
        self.v0=v0
        self.Theta=theta
        self.theta=theta*np.pi/180
        self.vx0=self.v0*np.cos(self.theta)
        self.vy0=0
        self.vz0=self.v0*np.sin(self.theta)
        self.dt=0.01
        return None
    
    def B2m(self,v):#it means B2/m
        return 0.0039+0.0058/(1+np.exp((v-vd)/Delta))
    def a(self,vx,vy,vz):
        vxyz=np.sqrt(vx**2+vy**2+vz**2)
        ax=-self.B2m(vxyz)*np.sqrt((vx-v_wind)**2+vy**2+vz**2)*(vx-v_wind)-S0m*omega*vy
        ay=-self.B2m(vxyz)*np.sqrt((vx-v_wind)**2+vy**2+vz**2)*vy+S0m*omega*(vx-v_wind)
        az=-g
        return ax,ay,az
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Z=[self.z0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.Vz=[self.vz0]
        self.T=[0]
        while not (self.Z[-1]<self.zFinal and self.Vz[-1]<0):
            newVx=self.Vx[-1]+self.a(vx=self.Vx[-1],vy=self.Vy[-1],vz=self.Vz[-1])[0]*self.dt
            newVy=self.Vy[-1]+self.a(vx=self.Vx[-1],vy=self.Vy[-1],vz=self.Vz[-1])[1]*self.dt
            newVz=self.Vz[-1]-g*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.Vz.append(newVz)
            newX=self.X[-1]+self.Vx[-1]*self.dt
            newY=self.Y[-1]+self.Vy[-1]*self.dt
            newZ=self.Z[-1]+self.Vz[-1]*self.dt
            self.X.append(newX)
            self.Y.append(newY)
            self.Z.append(newZ)
        self.Z[-1]=self.zFinal
        return 0
    def distance(self):
        return self.X[-1]
    def y_shifting(self):
        return self.Y[-1]
    def height(self):
        return max(self.Z) 
    def plot_3d(self, color):
        plt.plot(self.X,self.Y,self.Z,color,label=(self.v0,self.Theta))
        plt.legend(loc='best')
        return 0
    
'''    def trace(self):
        global x,y
        x=[]
        y=[]
        for t in self.'''

theta=np.linspace(15,75,12)
f=[]
for i in range (len(theta)):
    k=baseball(40,theta[i],0)
    k.fly()
    plt.plot(k.X,k.Y,k.Z,label=r'$\theta=%.2f^\circ$'%theta[i])
    plt.xlabel('x(m)',fontsize=14)
    plt.ylabel('y(m)',fontsize=14)
    ax.set_zlabel('z(m)',fontsize=14)
    plt.legend(loc='best',frameon=False)
    f.append(k.Y[-1])

plt.title('A batted ball with side spin',fontsize=24)    
plt.show()

phi=np.linspace(13.5,73.5,12)
width=3
plt.bar(phi,f,width,color='r')
plt.xlabel(r'$\theta^\circ$')
plt.ylabel('the maximum range of y')
plt.title('the maximum ranges of y at different initial angles')
plt.show()



'''A=baseball(100,45)
A.fly()
A.plot('g')

B=baseball1(100,45)
B.fly()
B.plot('b')
plt.legend(loc='upper right',frameon=False)
plt.show()

print A.distance()
print A.height()
print B.distance()
print B.height()
'''

