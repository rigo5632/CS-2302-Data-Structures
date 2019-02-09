# Lab 1
# By: Rigobeto Quiroz
# Class: 1:30 PM - 2:50 PM MW
# This program will draw five circles inside and original circle,
# then inside those circles, 5 new circles will be generated and so on.
# Since we have 3 cricles horizontally and vertically, we have to
# cut each section in thirds, affecting the radius and the center at the same time. 

import matplotlib.pyplot as plt
import numpy as np
import math
def circle(a,b,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = a+rad*np.sin(t)
    y = b+rad*np.cos(t)
    return x,y
def draw_circles(ax,n,a,b,radius,w):
    if n>0:
        x,y = circle(a,b,radius)
        ax.plot(x,y,color='k')
        # Original and center circle
        draw_circles(ax,n-1,a,b,radius*w,w)
        # Right Circle
        draw_circles(ax,n-1,a+(radius*.66),b,radius*.w,w)
        # Left Cricle
        draw_circles(ax,n-1,a-(radius*.66),b,radius*.w,w)
        # Top Circle
        draw_circles(ax,n-1,a,b+(radius*.66),radius*.w,w)
        # Bottom Circle
        draw_circles(ax,n-1,a,b-(radius*.66),radius*.w,w)
plt.close("all")
fig, ax = plt.subplots()
calls = int(input('Enter number of recursion calls: '))
a = 100
b = 0
radius = 100
draw_circles(ax,calls,a,b,radius,.33)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
