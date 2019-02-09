# Lab 1
# By: Rigobeto Quiroz
# Class: 1:30 PM - 2:50 PM MW
# This program will draw a binary Tree. The tree will create a center point
# and will generate branches to the left and to the right according to center point
# the more recursion calls the more branches the tree will have. Each branch will have
# two children and so fourth.

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
        #Recursion calls for right and left branches
        binaryTree(ax,x-dx,y-dy,dx/2,dy,n-1)
        binaryTree(ax,x+dx,y-dy,dx/2,dy,n-1)
plt.close("all")
calls = int(input('Enter number of recursion calls?'))
# x,y - coordinate for midpoints or root
x = 50
y = 100
# dx, dy - Affects the next figures Xand Y directions
dx = x / 2
dy = y * calls
fig, ax = plt.subplots()
binaryTree(ax,x,y,x,dy,calls)
plt.axis('off')
plt.show()
