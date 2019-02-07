#Done
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
fig, ax = plt.subplots()
draw_circles(ax,7, [100,0], 100,.7)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
'''
#Done:
# 3A. n = 3
# 3B. n = 4
# 3C. n = 7
import matplotlib.pyplot as plt
import numpy as np
def binaryTree(ax,x,y,dx,dy,n):
    if n > 0:
        #Draws root and left branch
        ax.plot((x,x-dx),(y,y-dy),color='k')
        #Draws root and right branch
        ax.plot((x,x+dx),(y,y-dy),color='k')
        binaryTree(ax,x-dx,y-dy,dx/2,dy,n-1)
        binaryTree(ax,x+dx,y-dy,dx/2,dy,n-1)
plt.close("all")
n = 7
# x,y - coordinate for midpoints or root
x = 50
y = 100
# dx, dy - Affects the next figures Xand Y directions
dx = x / 2
dy = y * n
fig, ax = plt.subplots()
binaryTree(ax,x,y,dx,dy,n)
plt.show()
'''
'''
# Done
# 1.A 2 5
# 1.B 3 5
# 1.C 4, 5
import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,x,y,n,w):
    if n>0:
        #Draws square according to midpoint(x,y)
        ax.plot((x-w,x-w,x+w,x+w,x-w),(y-w,y+w,y+w,y-w,y-w),color='k')
        #Bottom left Square
        draw_squares(ax,(x-w),(y-w),n-1,(w/2))
        #Top left Square
        draw_squares(ax,(x-w),(y+w),n-1,(w/2))
        # Top Right Square
        draw_squares(ax,x+w,y+w,n-1,(w/2))
        # Bottom Right Square
        draw_squares(ax,x+w,y-w,n-1,(w/2))
plt.close("all")
fig, ax = plt.subplots()
# x,y - midpoint of Square
x = 0
y = 0
calls = int(input('Enter number of recusion calls?'))
draw_squares(ax,x,y,calls,5)
ax.set_aspect(1.0)
plt.show()
'''
'''
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
        print(a,b)
        x,y = circle(a,b,radius)
        ax.plot(a,b,color='k')
        draw_circles(ax,n-1,a,b,radius*w,w)
        draw_circles(ax,n-1,a,b*w,radius*w,w)
        draw_circles(ax,n-1,a,b,radius*w,w)
        draw_circles(ax,n-1,a*w,b,radius*w,w)
        draw_circles(ax,n-1,a-6.7,b,radius*w,w)
plt.close("all")
fig, ax = plt.subplots()
a = 10
b = 10
radius = 10
draw_circles(ax,3,a,b,radius,.33)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')
'''
