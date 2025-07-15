import numpy as np
from random import random
import matplotlib.pyplot as plt
from numba import njit
Lx=12
Ly=12
L=12
N=64

x=np.zeros(64)
y=np.zeros(64)
x[0]=random()*L
y[0]=random()*L
q=1

@njit
def f(x1,x2):
    dx=x1-x2
    if dx > 0.5*L:
        return dx-L
    elif dx < -0.5*L:
        return dx+L
    else:
        return dx

while q<=N:
    xx=random()*L
    yy=random()*L
    flag=1
    for i in range(0,q):
        d1=f(xx,x[i])
        d2=f(yy,y[i])
        
        if (d1**2+d2**2)<=2**(1/2)   :
            flag=0
            i=q
    if flag==1:
        x[q-1]=xx
        y[q-1]=yy
        q+=1
            
vx=np.zeros(N)
vy=np.zeros(N)
vcx=0
vcy=0

for i in range(0,N):
    vx[i]=(random()-0.5)
    vy[i]=(random()-0.5)
    vcx=vcx+vx[i]
    vcy=vcy+vy[i]
vcx=vcx/N
vcy=vcy/N
for i in range(0,N):
    vx[i]=vx[i]-vcx
    vy[i]=vy[i]-vcy
KE0=0
for i in range(0,N):
    KE0+=(vx[i]**2)+(vy[i]**2)
KE0=0.5*KE0
KE=2.2*63
SC=np.sqrt(KE/KE0)
for i in range(0,N):
    vx[i]=vx[i]*SC
    vy[i]=vy[i]*SC



#print(f(10,0))    
@njit   
def force(dx,dy):
    r=np.sqrt(dx**2+dy**2)
    ff=(24/r)*(2/(r**12)-(1/(r**6)))
    fx=ff*(dx/r)
    fy=ff*(dy/r)
    return fx,fy
@njit
def ac(x1,y1,x2,y2):
    dx=f(x1,x2)
    dy=f(y1,y2)
    return force(dx,dy)
@njit    
def verlet(x,v,a2,a1,dt):
    x = x + (v * dt) + (0.5 * a2 * (dt ** 2))
    v = v + (0.5 * (a2+a1) * dt)
    return x, v


#print(force(10,4))
dt=0.001
t=0
ax=np.zeros(N)
ay=np.zeros(N)
step=1
open("traj.xyz", "w")
out=open("traj.xyz", "a+")
while t<=40000*dt:
    ax=np.zeros(N)
    ay=np.zeros(N)
    for i in range(0,N-1):
        for j in range(i+1,N):
            a1, a2=ac(x[i],y[i],x[j],y[j])            
            ax[i]=ax[i]+a1
            ay[i]=ay[i]+a2
            ax[j]=ax[j]-a1
            ay[j]=ay[j]-a2
    if t==0 :
        axx=np.copy(ax)
        ayy=np.copy(ay)
    #print(ax[19],x[19],y[19] )
    for i in range(0, N):
        x[i], vx[i] = verlet(x[i],vx[i],ax[i],axx[i],dt)
        y[i], vy[i] = verlet(y[i], vy[i], ay[i], ayy[i], dt)
        if x[i] > L:
            x[i] = x[i] - L
        elif x[i] < 0:
            x[i] = x[i] + L
        if y[i] >=L:
            y[i] = y[i] - L
        elif y[i] <0:
            y[i] = y[i] + L
    axx=np.copy(ax)
    ayy=np.copy(ay)
    #vcx=0
    #vcy=0
    
    #vcx=sum(vx)/N
    #vcy=sum(vy)/N
    #vx=vx-vcx
    #vy=vy-vcy
    
    #print(vx[10])
    t+=dt
    if t%(1000*dt)<=10e-3 and t!=0:      
        vx=0.9*vx
        vy=0.9*vy         

    
    if t%(20*dt)<=10e-4 :
        out.write("64 \nMD, step=%d\n" % (step))
        step+=1
        for i in range(0,N):
            out.write("Ar %f %f 0 \n" %(x[i], y[i]))
    #plt.cla()
    #plt.axis([0,12,0,12])
    #plt.plot(x,y,'bo') 
    #plt.pause(0.0001)
out.close()
    
        
    
