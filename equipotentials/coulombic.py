import numpy as np
from scipy import integrate
from matplotlib import pyplot as plt
plt.style.use('seaborn-white')
import matplotlib as mpl

font = {'family': 'Liberation Sans',
        'weight': 'normal',
        'size': 21,
        }
        
eps_0 = 8e-12
#fac = (1./(4*np.pi*eps_0))
fac = 330.72/78
e= 1.602*1e-19


charges = np.ones(300)

for i in range(len(charges)):
	charges[i]=-1.00
	
qx=np.arange(-600,600,4)


qy=np.zeros(300)


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
    
    #Ex = fac * q * (dist_vec_x/dist**3)
    #Ey = fac * q * (dist_vec_y/dist**3)
    Et = fac * q * (1/dist)
    
    #sumEx += Ex
    #sumEy += Ey
    sumE += Et
for i in range(len(X)):
	for j in range(len(Y)):
		if sumE[i][j] < -30:
			sumE[i][j]=-30
# PLOT
plt.figure(figsize=(13,7))
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.streamplot(X,Y,sumEx,sumEy)
#plt.contour(X, Y, sumE, colors='blue');
#y_ticks = np.arange(-5e-9, 5e-9, 0.5e-9)
#plt.yticks(y_ticks)
plt.contour(X, Y, sumE, 50, cmap='jet');
clb=plt.colorbar()
#plt.xlabel('z (Angstrom)')
plt.ylabel('x ($\AA$)', fontdict=font)
#plt.text(-39.9,36, "(a)",weight="bold",fontsize= 'xx-large')
plt.title('(a)',loc='left',weight="bold", fontsize='20')
clb.ax.tick_params(labelsize=15)
clb.set_label('Kcal/mol', rotation=90, horizontalalignment='center' ,fontdict=font)
plt.legend(prop=font)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.savefig('coulombic',  dpi=400)
plt.show()

