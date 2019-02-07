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
#Done:
# 3A. n = 3
# 3B. n = 4
# 3C. n = 7
'''
import matplotlib.pyplot as plt
import numpy as np
import math

def binaryTree(ax,x,y,dx,dy,n):
    if n > 0:
        ax.plot((x,x-dx),(y,y-dy),color='k')
        ax.plot((x,x+dx),(y,y-dy),color='k')
        binaryTree(ax,x-dx,y-dy,dx/2,dy,n-1)
        binaryTree(ax,x+dx,y-dy,dx/2,dy,n-1)

plt.close("all")
n = 7
x = 50
y = 100
dx = x / 2
dy = y * n
fig, ax = plt.subplots()
binaryTree(ax,x,y,dx,dy,n)
plt.show()
'''
# Almost Done
# 1.A 2 5
# 1.B 3 5
# 1.C
import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,x,y,n,w):
    if n>0:
        ax.plot((x-w,x-w,x+w,x+w,x-w),(y-w,y+w,y+w,y-w,y-w),color='k')
        draw_squares(ax,x-w,y-w,n-1,w-2)
        draw_squares(ax,x-w,y+w,n-1,w-2)
        draw_squares(ax,x+w,y+w,n-1,w-2)
        draw_squares(ax,x+w,y-w,n-1,w-2)
plt.close("all")
fig, ax = plt.subplots()
x = 0
y = 0
draw_squares(ax,x,y,2,5)
ax.set_aspect(1.0)
plt.show()
