from scipy import constants
import math
import numpy as np
import matplotlib.pyplot as plt
h = constants.h
c = constants.c
e = math.e
pi = math.pi
k = constants.k
T = 1

def plank(v):
    return (2*h*v**3/(c**2*(np.exp(h*v/(k*T))-1)))

def reyleigh(v):
    return (2*v**2*k*T/c**2)

def wien(v):
    return (2*h*v**3/(c**2*np.exp(h*v/(k*T))))

t = np.logspace(0,8,9)
v = np.logspace(0,22,500)

color = ['black', 'lightcoral', 'red', 'saddlebrown', 'gold', 'green', 'orange', 'teal', 'blue']
for i in range(len(t)):
    T = t[i]
    plt.plot(v, plank(v),color=color[i],label='T = 10e%d'%i)
    plt.plot(v, reyleigh(v),':',color=color[i])
    plt.plot(v, wien(v),'--',color=color[i])
    plt.yscale('log')
    plt.xscale('log')
plt.title(r'$log_{10}(I_\nu)\;vs\; log_{\nu}$ for black body')
plt.legend()
#plt.xlim([1e2,1e22])
plt.ylim([1e-25,1e8])
plt.ylabel('Specific Intensity ($Jm^{-2}s^{-1}Hz^{-1}sr^{-1}$)')
plt.xlabel('Frequency (Hz)')
plt.savefig('Plot_q5.png')
plt.show()
