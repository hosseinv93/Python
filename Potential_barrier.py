#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
N=500
q=1 #number of barriers
xmin=0
xmax=9.4486 #bohr
L=q*xmax
a=1.8897   #bohr

wlist=np.zeros([5,10]) # eigenvalues
Nlist=np.arange(100,1100,100)
u=0 
 
for N in Nlist:
    h=(L-xmin)/N
    c0=1/(h**2)
    c1=-1/(2*(h**2))
    x=np.arange(xmin,L,h)
    T=c0*np.diag(np.ones(N-1))+c1*np.diag(np.ones(N-2),1)+c1*np.diag(np.ones(N-2),-1)
    V=np.zeros([N-1,N-1])


    j=0
    while j<q:
        for i in range(0,N-1):
            if (j*xmax+xmax/2-a/2)<=x[i]<=(j*xmax+xmax/2+a/2):
                V[i][i]=0.1837  #hartree
        j=j+1
    H=T+V
    val=la.eigvalsh(H)
    w,z=la.eigh(H)
    for T in range(0,5):
        wlist[T][u]=(val[T]*27.2113)
     
    u+=1


#print 5 first eigenvalues
print(val[0:5]*27.2113)    
vv=[0]
zlist=np.zeros([N,5])
for i in range(0,N-1):
    vv.append(V[i][i])
    for o in range(5):
        zlist[i][o]=z[:,o][i]


#print eigenvalues of energy based on N
for zz in range(0,5):
    ff=zz+1
    plt.figure(figsize=(4,2))
    plt.plot(Nlist,wlist[zz,:])
    plt.ylabel("E(eV)")
    plt.xlabel("N")
    plt.title('$E_{%i}$' %ff)
    #plt.legend()


#print(wlist[4,:])

#print potential and wavefunctions
plt.figure(figsize=(20,10))
plt.plot(x,vv,label="potential")
plt.plot(x,zlist[:,0],label="$\psi_{1}(x)$")
plt.plot(x,zlist[:,1],label="$\psi_{2}(x)$")
plt.plot(x,zlist[:,2],label="$\psi_{3}(x)$")
plt.plot(x,zlist[:,3],label="$\psi_{4}(x)$")
plt.plot(x,zlist[:,4],label="$\psi_{5}(x)$")
plt.xlabel("x")
plt.legend()


# In[ ]:





# In[ ]:




