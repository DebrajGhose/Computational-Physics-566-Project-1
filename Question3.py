# -*- coding: utf-8 -*-


from pylab import *
from scipy.optimize import curve_fit

seed() #random seed

#functions

#generate new particle

def generate_particle(size,dx):
    
    theta = rand()*2*pi #generate an angle between 0 and 2pi
    
    posx = 100/dx*cos(theta) + size/2; posy = 100/dx*sin(theta) + size/2; #generate cartesian coordinates around origin size/2,size/2
    
    #enforce periodic boundary conditions; this is necessary for the rare instance when the partcle gets generated [50,100] or something similar
    
    posx = mod(int(posx),size); posy = mod(int(posy),size); #so if the particle goes over the edge, it will reneter from other side

    return int(posx), int(posy)
    
#do random walk

def do_the_cha_cha(size,posx,posy):
    
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
    
    posx = mod(posx,size); posy = mod(posy,size); #so if the particle goes over the edge, it will reneter from other side
    
    return posx, posy
        
        
    
#check adjacency to cluster

def check_cluster(posx,posy,size,domain,step):
    
    bx = mod(posx- 1,size); fx = mod(posx + 1,size); #pixels behind or in front of x and y positions of particle
    by = mod(posy- 1,size) ; fy = mod(posy+ 1,size);


    if domain[bx,posy] > 0 or domain[fx,posy] > 0 or domain[posx,by] > 0 or domain[posx,fy] > 0: #check if there is an adjacent cluster
        
        domain[posx,posy] = step #cluster is established

    return domain


#3b

def frac_dim_plot(domain,size,sim):
    print "doing frac_dim"
    
def frac_dim_plot(domain,size):
    #Extract the mass of the fractal as a function of radius 
	
    masslist = []
    controlmasslist = [] #positive control to make sure my fit gives me some value close to 2
    rs = list(np.linspace(1,100/dx,100/dx))
	
    for r in rs:
        control_mass = 0
        mass = 0
        for m in range(1,size):
            for n in range(1,size):
                
                if ((m-size/2)**2 + (n-size/2)**2)**.5 < r:
                    control_mass = control_mass + 1
                 
                
                if domain[m,n] > 0 and ((m-size/2)**2 + (n-size/2)**2)**.5 < r:
                    mass = mass + 1
		
        masslist.append(mass)
        controlmasslist.append(control_mass)
    
    #do a fit
    popt1,pcov = curve_fit(log_fit,rs,controlmasslist) #this is just a positive control
    
    popt, pcov = curve_fit(log_fit,rs,masslist)
    plt.figure(sim+10)
    plt.plot(rs,masslist)
    plt.xlabel('Radius (pixels)')
    plt.ylabel('Mass')
    plt.title(str(popt[0]))
    clustername = 'Cluster' + str(sim) + 'dim.pdf'
    savefig(clustername)
    
    print 'Dimensionality of circle:'
    print popt1
    print 'Dimensionality of cluster:'
    print popt
    
    return popt[0]


def log_fit(r,df): #fit to find dimeinsionality where dimensionality of a circle is 2
    
    return pi*r**df
    

#----------------------------------
#               MAIN
#----------------------------------    
    

#3a


#set up domain

L = 200 #length units
dx = 2 #space discretization
size = int(L/dx) #size of domain in pixels

for sim in range(1,11):
    
    domain = zeros((size,size)) #0 is empty space and anything higher is 'stuff'
    domain[size/2,size/2] = 800000; #this going to be my seed, choose some value larger than zero
    fractal_dimensions = []


    cluster_reach = 0 #cluster growth parameter, when this gets big, we terminate
    
    step = domain[size/2,size/2] #this will keep track of time and add pretty pretty colors
    
    #first, generate particle on a ring of radius 100 units
    
    
    posx, posy = generate_particle(size,dx) #generate particle on a ring of radius 100
    
    
    while round(cluster_reach)<100/dx: #terminate when cluster reaches some size
        
        step = step + 1
        #check for cluster adjcency
        
        domain = check_cluster(posx,posy,size,domain,step)
        
        if domain[posx,posy] > 1: #generate new particle if spot is taken
        
            cluster_reach = np.linalg.norm([posx-size/2,posy-size/2]) #see how large cluster is
    
            posx, posy = generate_particle(size,dx) #generate particle on a ring of radius 100
    
        #do the random walk
        
        posx, posy = do_the_cha_cha(size,posx,posy) #NOTE: No need of particle decay since we enforced periodic boundary conditions
        
    fracapp = frac_dim_plot(domain,size,sim)
    
    fractal_dimensions.append(fracapp) #store dimensional values
    
    plt.figure(sim)
    plt.imshow(domain)
    plt.colorbar()
    plt.xlabel('Pixel = Length/dx')
    plt.ylabel('Pixel = Length/dx')
    clustername = 'Cluster' + str(sim) + '.pdf'
    savefig(clustername)


print 'Average df is:'
print np.mean(fractal_dimensions)












