# -*- coding: utf-8 -*-


from pylab import *

#generate seed based on current time

seed()

#simulation parameters

steps = 100 #number of steps for the walkers

simulations = 10000 #number of simulations you will run

store_msd = linspace(0,0,steps) #array to store MSDS

#create a random walker

walk_x = linspace(0,0,steps); walk_y = linspace(0,0,steps); #x and y locations of the random walker


for sims in range(1,simulations):
    
    for i in range(1,steps):
    
        dir_x = rand()-0.5; dir_y = rand()-0.5; #generate random x and y coordinates in [-0.5,0.5] to advance your walker
        
        norm_dir_x = dir_x/(sqrt(dir_x**2 + dir_y**2)); norm_dir_y = dir_y/(sqrt(dir_x**2 + dir_y**2)); #normalize movement vector
        
        
        #Now, advance walker
        
        walk_x[i] = walk_x[i-1] + norm_dir_x
        walk_y[i] = walk_y[i-1] + norm_dir_y

        msd = walk_x[i]**2 + walk_y[i]**2 #since the origin is [0,0], don't need to subtract intial time step
        

        store_msd[i] = (store_msd[i]*(sims - 1) + msd)/sims #find average msd

x_axis = range(3,steps)

plt.plot(x_axis,store_msd[3:steps]) #random walker works!
plt.xlabel('Simulation steps')
plt.ylabel('Mean square displacement (pixels^2)')

savefig('2Drandomwalk.pdf')
