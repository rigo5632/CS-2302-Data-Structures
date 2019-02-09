# Lab 1
# By: Rigobeto Quiroz
# Class: 1:30 PM - 2:50 PM MW
# This program draws smaller circles to the left for each recursion call.
# The more recursion calls and the amount you want to affect your radius
# and center will cause the circles to change the output.

#2A: 7, .7
#2B. 45, .95
#2C. 220, .98
import matplotlib.pyplot as plt
import numpy as np
import math
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        # Moves the center of the circle to the left. Only affects indexs 0, b/c of the x direction
        center[0] = center[0] * (w * w)
        # Makes Circle smaller
        radius = radius * w
        # Each recusion call the circle becomes smaller and moves further left
        draw_circles(ax,n-1,center,radius*w,w)
plt.close("all")
calls = int(input('Please enter number of recursion calls.'))
# affects radius and how much the circles move to the left
rateOfChange = float(input('Please enter the rate of which the circles are going to be affected.'))
fig, ax = plt.subplots()
draw_circles(ax,calls, [100,0], 100,rateOfChange)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
