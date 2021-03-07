import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
plt.style.use('seaborn-white')
from matplotlib import cm
font = {'family': 'Liberation Sans',
        'weight': 'normal',
        'size': 21,
        }

eps_0 = 8e-12
fac = (1./(4*np.pi*eps_0))
e = 1.602*1e-19
eps =0.1
sig =11.175

charges = np.ones(500)

#for i in range(len(charges)):
#	charges[i]=-1.00*e
	
qx=np.arange(-1000,1000,4)


qy=np.zeros(500)


print(len(charges),len(qx),len(qy))





#charges  = [-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0]
#qx       = [-4.0,-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0]
#qy       = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

# GRID
gridsize = 30
N = 500
X,Y = np.meshgrid( np.linspace(-gridsize,gridsize,N),
                   np.linspace(-gridsize,gridsize,N))
                   
# CALC E-FIELD   
sumEx = np.zeros_like(X)
sumEy = np.zeros_like(Y)

sumE = np.zeros_like(X)

for q, qxi, qyi in zip(charges,qx,qy):
    dist_vec_x = X - qxi
    dist_vec_y = Y - qyi 
    dist = np.sqrt(dist_vec_x**2 + dist_vec_y**2)
    dist[np.abs(dist) > 2**(1/6)*sig]=1e30
    #Ex = fac * q * (dist_vec_x/dist**3)
    #Ey = fac * q * (dist_vec_y/dist**3)
    Etl = 4 * eps * ((sig/dist)**12-(sig/dist)**6)
    #Etq = fac * q * (1/dist)
    #print(dist.shape)
    for i in range(len(Etl)):
    	for j in range(len(Etl)):
    		if dist[i][j]<=2**(1/6)*sig:
    			Etl[i][j] +=eps
    #sumEx += Ex
    #sumEy += Ey
    sumE += Etl 
#sumE -= np.min(sumE)
print(Etl.shape)
print(np.max(sumE)) 
print(np.min(sumE))
for i in range(len(X)):
	for j in range(len(Y)):
		if sumE[i][j] > 15:
			sumE[i][j]=15    
#print(sumE)
# PLOT
plt.figure(figsize=(13,7))
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.streamplot(X,Y,sumEx,sumEy)
#plt.contour(X, Y, sumE, colors='blue');
#y_ticks = np.arange(-5e-9, 5e-9, 0.5e-9)
#plt.yticks(y_ticks)
plt.contour(X, Y, sumE, 400, cmap='jet');
#plt.imshow(sumE)
clb=plt.colorbar()
#plt.xlabel('z (Angstrom)')
plt.ylabel('x ($\AA$)', fontdict=font)
plt.title('(b)',loc='left',weight="bold", fontsize='20')
clb.ax.tick_params(labelsize=15)
clb.set_label('Kcal/mol', rotation=90, horizontalalignment='center' ,fontdict=font)
#plt.fill_between(x[:,10],y[:,100], color='#539ecd')
#plt.clim(0, 15,1)
#plt.text(-39.9,36, "(b)",weight="bold",fontsize= 'xx-large')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(prop=font)
plt.savefig('Lennard-jones',  dpi=400)
plt.show()
