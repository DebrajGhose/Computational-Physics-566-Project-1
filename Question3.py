# -*- coding: utf-8 -*-


from pylab import *


#functions

#generate new particle

def generate_particle(size):
    
    posx = randint(0, size) - size/2; posy = randint(0, size) - size/2; #x and y positions of the particle

    mag = np.linalg.norm([posx,posy]) #magnitude from origin of domain
    
    k = 100/mag #constant to make the points fall on a circle of radius 100
    
    posx = k*posx + size/2; posy = k*posy + size/2; #now particle is on circle of radius 100 pixels

    return posx, posy
    
#do random walk

def do_the_cha_cha(size,posx.posy):
    
    step = randint(1,5) #choose one of four places for the patch to move to 
    
    if step == 1:
        
        posx = posx + 1
        
    elif step == 2:
        
        posx = posx - 1
        
    elif step == 3:
        
        posy = posy + 1
        
    elif step == 4:
        
        posy = posy - 1
        
    #enforce periodic boundary conditions
    
    posx = mod(posx-1,size) + 1; posy = mod(posy-1,size) + 1; #so if the particle goes over the edge, it will reneter from other side
    
    return posx, posy
        
        
    
#check adjacency to cluster

#assign new postiion to diffusing particle





#3a



#set up domain

size = 200 #size of domain

domain = zeros((size,size)) #0 is empty space and 1 is 'stuff'
domain[size/2,size/2] = 1; #this going to be my seed




#first, generate particle on a ring of radius 100 units


posx, posy = generate_particle(size) #generate particle on a ring of radius 100


for t in range(1,10): #replace with while loop later
    
    
    #check for cluster adjcency
    
    

    #do the random walk
    
    posx, posy = do_the_cha_cha(size,posx,posy) #NOTE: No need of particle decay since we enforced periodic boundary conditions
    











#3b
















##______________________________________________________________________________

#Test that generating particle on ring is working

"""
for t in range(1,10): #replace with while loop later
    
    posx, posy = generate_particle(size)
    
    mag = np.linalg.norm([posx-size/2,posy - size/2]) #magnitude from origin of domain

    print posx,posy,mag


"""














