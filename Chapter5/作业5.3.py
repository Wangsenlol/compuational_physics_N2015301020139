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

fig = plt.figure()
ax = fig.gca(projection='3d')
plt.figure()
CS = plt.contour(X,Y,Z,10)
plt.clabel(CS, inline=1, fontsize=12)
plt.title('Electric potential near two metal plates')
plt.xlabel('x(m)')
plt.ylabel('y(m)')



# Plot the 3D surface
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph
cset = ax.contour(X, Y, Z, zdir='z', offset=-1, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=240, cmap=cm.coolwarm)

ax.set_xlim(-40, 240)
ax.set_ylim(-40, 240)
ax.set_zlim(-1, 1)

ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
ax.set_zlabel('V')
ax.set_title('Electric potential distribution')
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
plt.show()