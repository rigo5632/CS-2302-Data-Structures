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
        draw_circles(ax,n-1,a,b,radius*w,w)
        draw_circles(ax,n-1,a+(radius*.66),b,radius*.33,w)
        draw_circles(ax,n-1,a-(radius*.66),b,radius*.33,w)
        draw_circles(ax,n-1,a,b+(radius*.66),radius*.33,w)
        draw_circles(ax,n-1,a,b-(radius*.66),radius*.33,w)
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
