#Done
#2A: 7, .7
#2B. 45, .95
#2C. 220, .98
'''
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
        center[0] = center[0] * (w * w)
        radius = radius * w
        draw_circles(ax,n-1,center,radius*w,w)

plt.close("all")
fig, ax = plt.subplots()
draw_circles(ax, 45, [100,0], 100,.95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
'''
'''
import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,p,c,og,a):
    if n ==  0:
        ax.plot(og[:,0],og[:,1],color='k')
    if n>0 and c == 0:
        p = (p / 2) -a
        print(p)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,p,c+1,og,a+7)
    if n>0 and c ==  1:
        p[:,1] = p[:,1] + a
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,p,c+1,og,a)
    if n>0 and c == 2:
        p[:,0] = p[:,0] + a
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,p,c+1,og,a)
    if n>0 and c == 3:
        p[:,1] = p[:,1] - a
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,p,c+1,og,a)
    if n > 0 and c >= 4:
        c = -1
        a = 2
        draw_squares(ax,n-1,p,c+1,og,a)


plt.close("all")
orig_size = 10
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares(ax,9,p,0,p,2)
#draw_squares(ax,[5,5],p,2)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squares.png')
'''
import matplotlib.pyplot as plt
import numpy as np
import math

def binaryTree(ax,p,n,w):
    if n > 0:
        ax.plot(p[:,0],p[:,1],color='k')
        p[0] = p[1]
        p[2] = p[1]
        p = p - 1
        binaryTree(ax,p,n-1,w)


plt.close("all")
orig_size = 10
p = np.array([[10,10],[9,9],[10,10],[11,9]])
fig, ax = plt.subplots()
binaryTree(ax,p,2,.5)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squares.png')
