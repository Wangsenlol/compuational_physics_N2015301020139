import matplotlib.pyplot as plt
import numpy as np  


q=0.5
l=9.8
g=9.8
omega_D=2/3
dt=0.04
FD=1.2

theta1 = [0.2]
omega1 = [0]
t = [0]
theta2= [0.201]
omega2= [0]
Delta=[0.001]
f=[3]
while t[-1] <= 150:
        omega1.append(omega1[-1] - (g/l)*np.sin(theta1[-1])*dt - q*omega1[-1]*dt +FD*np.sin(omega_D*t[-1])*dt)
        fuck1=theta1[-1] + (omega1[-1] )*dt
        omega2.append(omega2[-1] - (g/l)*np.sin(theta2[-1])*dt - q*omega2[-1]*dt +FD*np.sin(omega_D*t[-1])*dt)
        fuck2=theta2[-1] + (omega2[-1] )*dt
        t.append(t[-1] + dt)
        if fuck1<-np.pi and fuck2<-np.pi:        
            theta1.append(fuck1+2*np.pi)
            theta2.append(fuck2+2*np.pi)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
            
        elif fuck1<-np.pi and fuck2>np.pi:
            theta1.append(fuck1+2*np.pi)
            theta2.append(fuck2-2*np.pi)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
        elif fuck1>np.pi and fuck2>np.pi:
            theta1.append(fuck1-2*np.pi)
            theta2.append(fuck2-2*np.pi)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
        elif fuck1>np.pi and fuck2<-np.pi:
            theta1.append(fuck1-2*np.pi)
            theta2.append(fuck2+2*np.pi)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
        elif fuck1>np.pi and -np.pi<=fuck2<=np.pi:
            theta1.append(fuck1-2*np.pi)
            theta2.append(fuck2)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
        elif fuck1<-np.pi and -np.pi<=fuck2<=np.pi:
             theta1.append(fuck1+2*np.pi)
             theta2.append(fuck2)
             Delta.append(theta2[-1]-theta1[-1])
             f.append(np.log10(Delta[-1]))
        elif -np.pi<=fuck1<=np.pi and fuck2>np.pi:
            theta1.append(fuck1)
            theta2.append(fuck2-2*np.pi)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
        elif -np.pi<=fuck1<=np.pi and fuck2<-np.pi:
            theta1.append(fuck1)
            theta2.append(fuck2+2*np.pi)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
        else:
            theta1.append(fuck1)
            theta2.append(fuck2)
            Delta.append(theta2[-1]-theta1[-1])
            f.append(np.log10(Delta[-1]))
                

plt.title('$\Theta$ versus $time$,$\omega$(0)=0')
ax=plt.subplot(111)              
line1=ax.plot(t,theta1,color="blue",label='$\Theta$(0)=0.2')
line2=ax.plot(t,theta2,color="orange",label='$\Theta$(0)=0.201')
plt.plot(t,theta1,color='blue')
plt.plot(t,theta2,color='orange')
plt.xlabel("$time(s)$")
plt.ylabel("$\Theta(radius)$")
plt.legend(loc='upper left')
plt.show()

fig, ax = plt.subplots()
ax.set_yscale('log')

plt.title('$\Delta$ $\Theta$ versus $time$')
plt.plot(t,Delta)
plt.xlabel('$time$(s)')
plt.ylabel('$\Delta$ $\Theta$(radians)')
plt.ylim(10^(-7),10)

plt.subplot(1,1,1)
plt.plot(t,f)
plt.xlabel('$time$(s)')
plt.ylabel('log($\Delta$ $\Theta$)')