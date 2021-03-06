# -*- coding: utf-8 -*-
"""Program to solve the 1D diffusion equation"""

from pylab import *
from scipy.optimize import curve_fit
import math


#define the gaussian expression 

def gauss(x,sigma,k):
    return k*np.exp(-x*x/(2*sigma**2))/math.sqrt(2*math.pi*sigma**2)

#simulation parameters


D = 2 #Diffusion constant
dt = 0.0005 #time discretization
L = 10 #length of domain

N = 100 #number of discrete points

x = linspace(-L/2,L/2,N) #x coordinate
dx = x[1] - x[0] #space discretization

k = D*dt/dx**2
conc = np.zeros(N) #concentration at current time step
conc1 = np.zeros(N) #concentration at next time step

#setting up intial conditions

conc[N/2-1:N/2+1] = 20 #concentration of chemical 
c0 = np.copy(conc[:]) # store initial condition to plot later
#Diffuse stuff

for t in range(1,1001): #t is time step
    
    for i in range(1,N-1): #i is index on x
        
        conc1[i] = conc[i] + (conc[i-1] - 2*conc[i] + conc[i+1])*k

    conc = np.copy(conc1[:]) #copy calculated concentration into your folder
    

    #extract plots for 5 different times
    
    if t == 50:
        
        c1 = np.copy(conc[:])
        
        sigma = curve_fit(gauss,x,c1)  #use a fit to get the sigma(t) of the normal distribuation
        
        print '(2Dt)^0.5 = ' + str(sqrt(2*D*t*dt))
        print 'Fit sigma = ' + str(abs(sigma[0][0]))
        
    elif t == 100:
        
        c2 = np.copy(conc[:])
        
        sigma = curve_fit(gauss,x,c2)
        
        print '(2Dt)^0.5 = ' + str(sqrt(2*D*t*dt))
        print 'Fit sigma = ' + str(abs(sigma[0][0]))
        
    elif t == 200:
        
        c3 = np.copy(conc[:])
        
        sigma = curve_fit(gauss,x,c3)
        
        print '(2Dt)^0.5 = ' + str(sqrt(2*D*t*dt))
        print 'Fit sigma = ' + str(abs(sigma[0][0]))
        
    elif t == 400:
        
        c4 = np.copy(conc[:])
        
        sigma = curve_fit(gauss,x,c4)
        
        print '(2Dt)^0.5 = ' + str(sqrt(2*D*t*dt))
        print 'Fit sigma = ' + str(abs(sigma[0][0]))
        
    elif t == 800:
        
        c5 = np.copy(conc[:])
        
        sigma = curve_fit(gauss,x,c5)
        
        print '(2Dt)^0.5 = ' + str(sqrt(2*D*t*dt))
        print 'Fit sigma = ' + str(abs(sigma[0][0]))
        
plt.figure(1)

plt.plot(x,c0,label= 'time = 0' )
plt.plot(x,c1,label= 'time = ' + str(50*dt) )
plt.plot(x,c2, label= 'time = ' + str(100*dt))
plt.plot(x,c3, label= 'time = ' + str(200*dt))
plt.plot(x,c4, label= 'time = ' + str(400*dt))
plt.plot(x,c5, label= 'time = ' + str(800*dt))
plt.legend()
plt.xlabel('Distance (pixels)')

plt.ylabel('Concentration (concentration units)')


savefig('diffusiongraph.pdf')


