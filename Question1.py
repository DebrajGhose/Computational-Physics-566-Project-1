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
store_abs_x = linspace(0,0,steps)
store_abs_x2 = linspace(0,0,steps)
#create a random walker

walk_x = linspace(0,0,steps); walk_y = linspace(0,0,steps); #x and y locations of the random walker


for sims in range(1,simulations):
    
    for i in range(1,steps):
        
        
        dir_x, dir_y = do_the_cha_cha()
        
        #Now, advance walker
        
        walk_x[i] = walk_x[i-1] + dir_x
        walk_y[i] = walk_y[i-1] + dir_y

        mdx = np.sqrt(walk_x[i]**2)
        msdx = walk_x[i]**2 #since the origin is [0,0], don't need to subtract intial time step
        
        
        store_abs_x[i] = (store_abs_x[i]*(sims-1) + mdx) #weighted average

        store_abs_x2[i] = (store_abs_x2[i]*(sims-1) + msdx)


        msd = walk_x[i]**2 + walk_y[i]**2 #since the origin is [0,0], don't need to subtract intial time step
        md = np.sqrt(walk_x[i]**2 + walk_y[i]**2)
        

        store_msd[i] = (store_msd[i]*(sims - 1) + msd)/sims #find average msd
        store_md[i] = (store_md[i]*(sims - 1) + md)/sims #find average displacement

x_axis = range(0,steps)





plt.figure(1,figsize=(8,5))
plt.plot(x_axis,store_msd,label='Simulated MSD (pixels^2)') #random walker works!
plt.xlabel('Simulation steps (time units)')
plt.ylabel('MSD or Absolute displacement')
plt.plot(x_axis,store_md,label='Mean displacement (pixels)')

plt.plot(x_axis,store_abs_x,label='<x> (pixels)')

plt.plot(x_axis,store_abs_x2,label='<x^2> (pixels^2)')


#plotting an eyeball fit assuming slope = 1
slope = 1
plt.plot(x_axis,slope*x_axis,label='Eyeball Fit to MSD (pixels^2)')

plt.legend(loc = 'top left')


savefig('2Drandomwalkmsd.pdf')





