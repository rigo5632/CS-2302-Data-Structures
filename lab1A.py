# Lab 1
# By: Rigobeto Quiroz
# Class: 1:30 PM - 2:50 PM MW
# This program draws squares at the corners of other square using recursion. The
# greater number of recursions the more squares the program is going to draw. Each
# recursion call > 1 creates 4 squares at the corners of the already sepcified squares.

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
plt.axis('off')
plt.show()
