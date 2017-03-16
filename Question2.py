# -*- coding: utf-8 -*-


from pylab import *

#question b

#simulation parameters


D = 2 #Diffusion constant
dt = 0.0005 #time discretization
L = 10 #length of domain

N = 100 #number of discrete points

x = linspace(-L/2,L/2,N) #x coordinate
dx = x[1] - x[0] #space discretization

k = D*dt/dx**2
conc = np.zeros(N) #concentration at current time step
conc1 = np.zeros(N) #conccentration at next time step

#setting up intial conditions

conc[N/2-5:N/2+5] = 10 #concentration of chemical 
c0 = np.copy(conc[:]) # store initial condition to plot later
#Diffuse stuff

for t in range(1,1000): #t is time step
    
    for i in range(1,N-1): #i is index on x
        
        conc1[i] = conc[i] + (conc[i-1] - 2*conc[i] + conc[i+1])*k

    conc = np.copy(conc1[:]) #copy calculated concentration into your folder
    

    #extract plots for 5 different times
    
    if t == 200:
        
        c1 = np.copy(conc[:])
        
    elif t == 450:
        
        c2 = np.copy(conc[:])
        
    elif t == 600:
        
        c3 = np.copy(conc[:])
        
    elif t == 800:
        
        c4 = np.copy(conc[:])
        
    elif t == 1000:
        
        c5 = np.copy(conc[:])

plt.figure(1)

plt.plot(x,c0,label= 't = 0' )
plt.plot(x,c1,label= 't = ' + str(200/dt) )
plt.plot(x,c2, label= 't = ' + str(450/dt))
plt.plot(x,c3, label= 't = ' + str(600/dt))
plt.plot(x,c4, label= 't = ' + str(800/dt))
plt.plot(x,c5, label= 't = ' + str(1000/dt))
plt.legend()

savefig('diffusiongraph.pdf')


