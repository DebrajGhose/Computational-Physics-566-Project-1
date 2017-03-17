# -*- coding: utf-8 -*-


from pylab import *

seed() #random seed

#functions

#generate new particle

def generate_particle(size,dx):
    
    posx = randint(0, size) - size/2; posy = randint(0, size) - size/2; #x and y positions of the particle

    mag = np.linalg.norm([posx,posy]) #magnitude from origin of domain
    
    k = 100/dx/mag #constant to make the points fall on a circle of radius 100
    
    posx = k*posx + size/2; posy = k*posy + size/2; #now particle is on circle of radius 100 pixels

    return int(posx), int(posy)
    
#do random walk

def do_the_cha_cha(size,posx,posy):
    
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
    
    posx = mod(posx,size); posy = mod(posy,size); #so if the particle goes over the edge, it will reneter from other side
    
    return posx, posy
        
        
    
#check adjacency to cluster

def check_cluster(posx,posy,size,domain):
    
    bx = mod(posx- 1,size); fx = mod(posx + 1,size); #pixels behind or in front of x and y positions of particle
    by = mod(posy- 1,size) ; fy = mod(posy+ 1,size);


    if domain[bx,posy] == 1 or domain[fx,posy] == 1 or domain[posx,by] == 1 or domain[posx,fy] == 1: #check if there is an adjacent cluster
        
        domain[posx,posy] = 1 #cluster is established

    return domain
    


#3a



#set up domain
L = 200 #length units
dx = 4 #space discretization
size = L/dx #size of domain in pixels

domain = zeros((size,size)) #0 is empty space and 1 is 'stuff'
domain[size/2,size/2] = 1; #this going to be my seed
cluster_reach = 0 #cluster growth parameter, when this gets big, we terminate



#first, generate particle on a ring of radius 100 units


posx, posy = generate_particle(size,dx) #generate particle on a ring of radius 100


while round(cluster_reach)<100/dx: #terminate when cluster reaches some size
    
    
    #check for cluster adjcency
    
    domain = check_cluster(posx,posy,size,domain)
    
    if domain[posx,posy] == 1: #generate new particle if spot is taken
    
        cluster_reach = np.linalg.norm([posx-size/2,posy-size/2]) #see how large cluster is

        posx, posy = generate_particle(size,dx) #generate particle on a ring of radius 100

    #do the random walk
    
    posx, posy = do_the_cha_cha(size,posx,posy) #NOTE: No need of particle decay since we enforced periodic boundary conditions
    


plt.imshow(domain)

savefig('Cluster1.pdf')

np.save('Cluster1',domain)






#3b
















##______________________________________________________________________________

#Test that generating particle on ring is working

"""
for t in range(1,10): #replace with while loop later
    
    posx, posy = generate_particle(size)
    
    mag = np.linalg.norm([posx-size/2,posy - size/2]) #magnitude from origin of domain

    print posx,posy,mag


"""














