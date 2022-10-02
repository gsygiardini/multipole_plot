#%reset -f
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline


fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.arange(-5, 5, 0.2),
                      np.arange(-5, 5, 0.2),
                      np.arange(-5, 5, 0.2))


k=1
Q=1
h=0.5

u = k*Q*x*(1/(np.sqrt(x**2+y**2+z**2))**3) - k*(1/3)*(Q*h**2)*(-x)*(1/(np.sqrt(x**2+y**2+z**2))**5) + k*(5/6)*(Q*h**2)*x*(-x**2-y**2+2*z**2)*(1/(np.sqrt(x**2+y**2+z**2))**7)
v = k*Q*y*(1/(np.sqrt(x**2+y**2+z**2))**3) - k*(1/3)*(Q*h**2)*(-y)*(1/(np.sqrt(x**2+y**2+z**2))**5) + k*(5/6)*(Q*h**2)*y*(-x**2-y**2+2*z**2)*(1/(np.sqrt(x**2+y**2+z**2))**7)
w = k*Q*z*(1/(np.sqrt(x**2+y**2+z**2))**3) - k*(1/3)*(Q*h**2)*(2*z)*(1/(np.sqrt(x**2+y**2+z**2))**5) + k*(5/6)*(Q*h**2)*z*(-x**2-y**2+2*z**2)*(1/(np.sqrt(x**2+y**2+z**2))**7)


ax.quiver(x, y, z, u, v, w, length=0.1, color = 'black')
#plt.streamplot(y,z,v,w, density=3, linewidth=None, color='#A23BEC')
#plt.title('Electromagnetic Field')
#plt.xlabel("Y")
#plt.ylabel("Z")

#plt.yticks([])
#plt.xticks([])
#plt.grid()

plt.show()
