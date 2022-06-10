# -*- coding: utf-8 -*-
"""
The Simplest Implementation of Conway's Game of Life

"""
import numpy as np
from scipy import signal 
import matplotlib.pyplot as plt

x_size = 200
y_size = 100
p = 0.05

# init
alive = np.random.rand(y_size, x_size) < p

kernel = np.array(
    [[1,1,1], 
     [1,0,1], 
     [1,1,1]])

for _ in range(1000):
    plt.imshow(alive.astype(int))
    plt.show()
    
    n_neighbours = signal.convolve2d(alive, kernel, mode='same', boundary='wrap')
    
    # any live cell with two or three live neighbours survives
    # any dead cell with three live neighbours becomes a live cell
    alive = np.logical_or(
        n_neighbours==3,
        np.logical_and(alive, n_neighbours==2)
        )
