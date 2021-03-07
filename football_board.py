import numpy as np
import matplotlib.pyplot as plt
r=3
a=0.1
@np.vectorize #this line is needed
def f(xs):
    if xs>=a*r:
        ys=np.sqrt(r**2-((xs-a*r)**2))
    elif -a*r<xs<a*r:
        ys=r
    else:
        ys=np.sqrt(r**2-((xs+a*r)**2))
    return ys
n=10000
xs=np.linspace(-a*r-r,a*r+r,n)
xs=np.append(xs,np.flip(xs))
ys=np.zeros(2*n)
for i in range(n):
    ys[i]=f(xs[i])
for i in range(n,2*n):
    ys[i]=-f(xs[i])
plt.plot(xs,ys)

gam=1000
x=0
y=0
vx=2
vy=2
dt=0.1
xlist=[0]
ylist=[0]
x2=1e-5
y2=0
vx2=2
vy2=2
x2list=[0]
y2list=[0]
def gradf(x,y):
    if x>=a*r:
        gradiant=(2*(x-a*r),2*y)
    elif -a*r<x<a*r and f(x)>=0:
        gradiant=(0,1)
    elif -a*r<x<a*r and f(x)<0:
        gradiant=(0,-1)
    else:
        gradiant=(2*(x+a*r),2*y)
    return gradiant/np.linalg.norm(gradiant)

def vout(vx,vy,x,y):
    vi=np.array([vx,vy])
    voi=(np.dot(vi,gradf(x,y)))*gradf(x,y)
    vpi=vi-voi
    vof=-voi
    vpf=vpi
    vf=vof+vpf
    return vf
xplist=[]
yplist=[]
xp2list=[]
yp2list=[]
t=0
while t<gam*dt:
    while -a*r-r<x<a*r+r and -f(x)<y<f(x):
        xlist.append(x)
        ylist.append(y)
        x+=vx*dt
        y+=vy*dt
        t+=dt
    dt=dt/20
    x=xlist[-1]
    y=ylist[-1]
    while -a*r-r<x<a*r+r and -f(x)<y<f(x):
        xplist.append(x)
        yplist.append(y)
        x+=vx*dt
        y+=vy*dt
    x=xplist[-1]
    y=yplist[-1]
    xlist.append(x)
    ylist.append(y)
    vf=vout(vx,vy,x,y)
    vx=vf[0]
    vy=vf[1]
    dt=dt*20
t=0
while t<gam*dt:
    while -a*r-r<x2<a*r+r and -f(x2)<y2<f(x2):
        x2list.append(x2)
        y2list.append(y2)
        x2+=vx2*dt
        y2+=vy2*dt
        t+=dt
    dt=dt/20
    x2=x2list[-1]
    y2=y2list[-1]
    while -a*r-r<x2<a*r+r and -f(x2)<y2<f(x2):
        xp2list.append(x2)
        yp2list.append(y2)
        x2+=vx2*dt
        y2+=vy2*dt
    x2=xp2list[-1]
    y2=yp2list[-1]
    x2list.append(x2)
    y2list.append(y2)
    vf2=vout(vx2,vy2,x2,y2)
    vx2=vf2[0]
    vy2=vf2[1]
    dt=dt*20
m=len(x2list)
xtlist=[]
ytlist=[]
xttlist=[]
yttlist=[]
for i in range(0,m):
    plt.cla()
    plt.plot(xs,ys)
    plt.plot(x2list[i],y2list[i],'bo')
    plt.plot(xlist[i],ylist[i],'ro')
    xttlist.append(x2list[i])
    yttlist.append(y2list[i])
    #plt.plot(xttlist,yttlist,'b')
    xtlist.append(xlist[i])
    ytlist.append(ylist[i])
    #plt.plot(xtlist,ytlist,'r') 
    plt.pause(0.01)
plt.show()
llist=[]
tlist=[]
tt=0
for j in range(0,gam):
    l=np.sqrt((x2list[j]-xlist[j])**2+(y2list[j]-ylist[j])**2)
    llist.append(l)
    tt=tt+j*0.1
    tlist.append(tt)
plt.figure(figsize=(3,3))
plt.plot(tlist,llist,'g')
print(vout(2,2,3,5))

