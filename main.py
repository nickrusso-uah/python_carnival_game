import random
import numpy as np

from bottle import Bottle
from ring import Ring
from allocate_rings import genetic_allocator

def main():
    #define some parameters 
    num_mcs = 1
    max_bottles = 5
    max_rings = 8
    num_runs = num_mcs + 1

    #define some ranges for the random number generator seeding bottle and ring sizes
    ring_size_range = np.array([0.6, 0.8])
    bottle_size_range = np.array([0.4, 0.6])
    #loop over the number of Monte Carlo runs, randomly define a scenario for each 
    for ii in range(1, num_runs):
        bottles = []
        rings =[]
        #define a random number of bottles for this MC, create a class instance for each 
        num_bottles = random.randint(1, max_bottles)
        for b in range(0, num_bottles):
            #randomly define a size and value for this bottle
            bottle_size = random.uniform(bottle_size_range[0], bottle_size_range[1])
            bottle_value = random.uniform(10, 20)
            #create the class instance 
            this_bottle = Bottle(bottle_size, bottle_value)
            bottles.append(this_bottle)
        #repeat for the rings
        for r in range(0, num_rings):
            num_rings = random.randint(1, max_rings)
            ring_size = random.uniform(ring_size_range[0], ring_size_range[1])
            this_ring = Ring(ring_size)
            rings.append(this_ring)
    
    #call the allocator
    genetic_allocator(rings, bottles)
        

if __name__ == "__main__":
    main()