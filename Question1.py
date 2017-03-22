# -*- coding: utf-8 -*-


from pylab import *


#Do the cha cha

def do_the_cha_cha():
    posx = 0; posy = 0;
    step = randint(1,5) #choose one of four directions for the patch to move to 
    
    if step == 1:
        
        posx = posx + 1
        
    elif step == 2:
        
        posx = posx - 1
        
    elif step == 3:
        
        posy = posy + 1
        
    elif step == 4:
        
        posy = posy - 1
        
    #enforce periodic boundary conditions
    
    return posx, posy


#generate seed based on current time

seed()

#simulation parameters

steps = 100 #number of steps for the walkers

simulations = 10000 #number of simulations you will run

store_md = linspace(0,0,steps) #array to store mean displacement 

store_msd = linspace(0,0,steps) #array to store mean square displacement MSDS

#create a random walker

walk_x = linspace(0,0,steps); walk_y = linspace(0,0,steps); #x and y locations of the random walker


for sims in range(1,simulations):
    
    for i in range(1,steps):
        
        
        dir_x, dir_y = do_the_cha_cha()
        
        #Now, advance walker
        
        walk_x[i] = walk_x[i-1] + dir_x
        walk_y[i] = walk_y[i-1] + dir_y

        msd = walk_x[i]**2 + walk_y[i]**2 #since the origin is [0,0], don't need to subtract intial time step
        md = np.sqrt(walk_x[i]**2 + walk_y[i]**2)
        

        store_msd[i] = (store_msd[i]*(sims - 1) + msd)/sims #find average msd
        
        store_md[i] = (store_md[i]*(sims - 1) + md)/sims #find average displacement

x_axis = range(3,steps)

plt.plot(x_axis,store_msd[3:steps]) #random walker works!
plt.xlabel('Simulation steps')
plt.ylabel('Mean square displacement (pixels^2)')

savefig('2Drandomwalkmsd.pdf')

plt.plot(x_axis,store_msd[3:steps]) #random walker works!
plt.xlabel('Simulation steps')
plt.ylabel('Mean displacement (pixels)')

savefig('2Drandomwalkmsd.pdf')


#Calculating and plotting a line of best fit to the data

linebestfit = np.poly1d(np.polyfit(x_axis, store_msd[3:steps], 1))(np.unique(x_axis))
#y intercept
b = linebestfit[0]
 
#find average slope
ms = 0
for i in range(len(linebestfit)):
	ms = ms + linebestfit[i]/x_axis[i]
m = ms/len(linebestfit) 

plt.plot(np.unique(x_axis), linebestfit, label= 'y = ' + str(m) + ' x + ' + str(b) )
plt.legend()
plt.xlabel('Simulation steps')
plt.ylabel('Mean square displacement (pixels^2)')
savefig('BestfitMSD')
