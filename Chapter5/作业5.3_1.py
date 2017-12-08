from __future__ import division
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


grid = []
for i in range(201):    
    row_i = []
    for j in range(201):
        if i == 0 or i == 200 or j == 0 or j == 200:
            voltage = 0
        elif 50<=i<=150 and j == 60:
            voltage = 1
        elif 50<=i<=150 and j == 140:
            voltage = -1
        else:
            voltage = 0
        row_i.append(voltage)
    grid.append(row_i)

# define the update_V function (Gauss-Seidel method)

def update_V(grid):

    delta_V = 0

    for i in range(201):    
        for j in range(201):
            if i == 0 or i == 200 or j == 0 or j == 200:
                pass
            elif 50<=i<=150 and j == 60:
                pass
            elif 50<=i<=150 and j == 140:
                pass
            else:
                voltage_new = (grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
                voltage_old = grid[i][j]
                delta_V += abs(voltage_new - voltage_old)
                grid[i][j] = voltage_new

    return grid, delta_V

# define the Laplace_calculate function

def Laplace_calculate(grid):

    epsilon = 10**(-5)*200**2
    grid_init = grid
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 10:
        grid_impr, delta_V = update_V(grid_init)
        grid_new, delta_V = update_V(grid_impr)
        grid_init = grid_new
        N_iter += 1

    return grid_new

x = np.linspace(0,200,201)
y = np.linspace(0,200,201)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(grid)

fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
ax = fig.gca(projection='3d')
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")

plt.tight_layout()
plt.show()


