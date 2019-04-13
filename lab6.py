# Author: Rigoberto Quiroz
# Section: 1:30 PM - 2:50 PM
# This program will create a create maze with x rows and y columns. Then we will
# create lists that contain values that are next to each other. Then we will create
# a Disjoint set and set a while loop that will check the number of sets until
# we have 1 remaining set (contains all sets). Loop will unionize the values in
# our lists, and remove the walls that separate them. Creating pathways that will
# connect points A to B, creating only one path. Once that is done we are going
#to draw the maze, along with printing its Disjoint Set.

import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Creates Disjoint Set according to the rows and columns of our maze
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1


def union(S,i,j):
    # roots of i and j
    ri = find(S,i)
    rj = find(S,j)
    # Do not belong in the same set
    if ri !=rj:
        # Union
        S[rj] = ri
        return
    # Belong in the same set
    return False

def find(S,i):
    # Finds the root of our index i
    if S[i] < 0:
        return i
    return find(S,S[i])

# Creates the max according to our x and y values
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off')
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

# Counts the number of Sets we have in our Disjoint Set
def numOfSets(S):
    count = 0
    # Count + 1, if value is a root
    for key in S:
        if key <= -1:
            count +=1
    return count

def find_c(S,i):
    # Finds root of i
    if S[i] < 0:
        return i
    # Sets all values in a set to its root, without going to other values in
    # the set
    r = find_c(S,S[i])
    S[i] = r
    return r

def unionBySize(S,i,j):
    # Finds root of i and j
    ri = find_c(S,i)
    rj = find_c(S,j)
    # do not belong in the same set
    if ri != rj:
        # Unionzing Set by size (Larger set)
        # Root j is gretaer than root i
        if -(S[ri]) < -(S[rj]):
            # Keeps track of length of sets
            S[rj] += S[ri]
            S[ri] = rj
            return
        else:
            # root i is greater than root j
            S[ri] += S[rj]
            S[rj] = ri
            return
    # Belong to the same set
    return False


plt.close("all")
# Creates Maze specs, x and y
maze_rows = 3
maze_cols = 3

walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True)

# User can choose which type of union to do, Standard, or compression
print('Which Disjoint set union do you want to apply:')
print('1. Standard Union')
print('2. Union by Size with path compression')
choice = int(input('Choice: '))

# Standard Union
if choice == 1:
    standardStart = time.time()
    # While we have more than 1 set
    while numOfSets(S) != 1:
        # Select a random list and unionize them
        d = random.randint(0,len(walls)-1)
        if union(S,walls[d][0],walls[d][1]) != False:
            print('removing wall ',walls[d])
            # remove them from lists
            walls.pop(d)
    # Final Disjoint Set, and maze drawing
    print(S)

    draw_maze(walls,maze_rows,maze_cols)

    standardEnd = time.time()

    print('Standard Union Time: ', standardEnd - standardStart)
    plt.show()
    exit(0)

# union by size and compression
if choice == 2:
    compressionStart = time.time()
    # While we have more than one set
    while numOfSets(S) != 1:
        # random list
        d = random.randint(0,len(walls)-1)
        # unionize items from random list
        if unionBySize(S,walls[d][0],walls[d][1]) != False:
            # remove from list
            print('removing wall ',walls[d])
            walls.pop(d)
    #Final Disjoint Set and maze
    print(S)

    draw_maze(walls,maze_rows,maze_cols)

    compressionEnd = time.time()

    print('Union by Size and compression time: ', compressionEnd - compressionStart)
    plt.show()
    exit(0)
else:
    # User selects something else than 1 or 2
    print('Invalid input')
    exit(0)
