# -*- coding: utf-8 -*-


from pylab import *


#functions

#generate new particle

def generate_particle(size):
    
    posx = randint(1, size) - size/2; posy = randint(1, size) - size/2; #x and y positions of the particle

    mag = np.linalg.norm([posx,posy]) #magnitude from origin of domain
    
    k = 100/mag #constant to make the points fall on a circle of radius 100
    
    posx = k*posx + size/2; posy = k*posy + size/2; #now particle is on circle of radius 100 pixels

    return posx, posy
    

#check adjacency to cluster

#assign new postiion to diffusing particle





#3a



#set up domain

size = 200 #size of domain

domain = zeros((size,size)) #0 is empty space and 1 is 'stuff'
domain[size/2,size/2] = 1; #this going to be my seed




#first, generate particle on a ring of radius 100 units


posx, posy = generate_particle(size)


for t in range(1,10): #replace with while loop later
    
    
    











#3b
















##______________________________________________________________________________

#Test that generating particle on ring is working

"""
for t in range(1,10): #replace with while loop later
    
    posx, posy = generate_particle(size)
    
    mag = np.linalg.norm([posx-size/2,posy - size/2]) #magnitude from origin of domain

    print posx,posy,mag


"""














