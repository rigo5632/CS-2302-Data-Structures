# Author: Rigoberto Quiroz
# Section: 1:30PM - 2:50 PM
# This program will create a BST(Binary Search Tree), and will(1) display the
# BST using matplotlib. Then(2) it will search for any key in a iterative way.
# (3) Then given a sorted native list in python it is going to create a BST.
# (4) Then it will extract the items of any BST into to list in ascending order.
# (5) Finally it will print items at a certain depth

import random
import matplotlib.pyplot as plt
import numpy as np

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T

def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)

def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        print(space,T.item)
        InOrderD(T.right,space+'   ')
        InOrderD(T.left,space+'   ')

def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T

def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)

def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

def IterativeSearch(T,key):
    temp = T
    # Looks for item in BST
    while temp is not None:
        # Key found
        if temp.item == key:
            return temp.item
        # Move right is key is greater than root
        elif key > temp.item:
            temp = temp.right
        else:
            # move left if less
            temp = temp.left
    return None

def sort(T,sL):
    if T is not None:
        sort(T.left,sL)
        #inserts BST items into list
        sL.append(T.item)
        sort(T.right,sL)
        return sL

def InOrder1(T,h):
    # Prints items in BST in ascending order
    if T is not None:
        #When we reach the desired depth we want to print
        if h == 0:
            print(T.item,end = ' ')
            return
        InOrder1(T.left,h-1)
        InOrder1(T.right,h-1)

def depth(T):
    if T is None:
        return -1
    # Calculates the depth of left and right branches
    left = 1 + depth(T.left)
    right = 1 + depth(T.right)
    # returns which ever was bigger
    if left > right:
        return left
    return right

def buildTree(L):
    if L is None:
        return
    if len(L) <= 0:
        return
    # Gets midpoint index of list
    midPoint = len(L)//2
    # Makes the midpoint the roo
    root = BST(L[midPoint])
    n = 0
    left = []
    right = []
    # Creates 2 list, midpoint is not included in neither of the list
    while n < len(L)//2:
        left.append(L[n])
        n = n + 1
    n = n + 1
    while n < len(L):
        right.append(L[n])
        n = n + 1
    # inserts the rest of the list items
    root.left = buildTree(left)
    root.right = buildTree(right)
    return root

def printBST(T,ax,x,y,dx,dy):
    if T is None:
        return
    # If the item is a leaf
    if T.left is None and T.right is None:
        ax.text(x,y,T.item,fontsize=7)
        ax.plot(x,y,'o',markersize=20,markeredgecolor='black',markerfacecolor='white')
        return
    # if we only have 1 children, right or left
    if T.left is None:
        ax.plot((x,x+dx),(y,y-dy),color='k')
        ax.text(x-1,y-1,T.item,fontsize=7)
        ax.plot(x,y,'o',markersize=20,markeredgecolor='black',markerfacecolor='white')
        printBST(T.right,ax,x+dx,y-dy,dx/2,dy)
        return
    if T.right is None:
        ax.plot((x,x-dx),(y,y-dy),color='k')
        ax.text(x,y,T.item,fontsize=7)
        ax.plot(x,y,'o',markersize=20,markeredgecolor='black',markerfacecolor='white')
        printBST(T.left,ax,x-dx,y-dy,dx/2,dy)
        return
    # if we have both children
    ax.plot((x,x-dx),(y,y-dy),color='k')
    ax.plot((x,x+dx),(y,y-dy),color='k')
    ax.text(x-1,y-1,T.item,fontsize=7)
    ax.plot(x,y,'o',markersize=20,markeredgecolor='black',markerfacecolor='white',label=T.item)

    printBST(T.left,ax,x-dx,y-dy,dx/2,dy)
    printBST(T.right,ax,x+dx,y-dy,dx/2,dy)

# Code to test the functions above
T = None
A = [10,4,15,2,8,12,18,1,3,5,9,7]
#A =[]
#A = [1,2,3,4]
for a in A:
    T = Insert(T,a)
plt.close("all")
B = None
L = [1,2,3,4,5]
B = buildTree(L)
x = 50
y = 100
dx = x / 2
dy = y * len(A)
fig, ax = plt.subplots()
print('Displaying BST Tree')
printBST(T,ax,x,y,dx,dy)
print('\n')
key = int(input('Enter key to search for in BST.'))
print('Looking for',key, 'in BST.')
print(IterativeSearch(T,key))
print('\n')
print('Building a BST from sorted list.')
L = [1,2,3,4,5]
B = buildTree(L)
#printBST(B,ax,x,y,dx,dy)
print('\n')
print('Creating a sorted native list from BST')
print(sort(T,[]))
print('\n')
dep = int(input('Enter depth.'))
print("Keys at Depth", dep,':',end=' ')
InOrder1(T,dep)
#print(sort(T,[]))
plt.axis('off')
plt.show()
