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
import graphs
import dsf

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

def adjList(V, cells):
    # Creates a list of size cells
    adjL = [[] for i in range(cells)]
    # Using the list that stored our removed cells, we are going to place those
    # cells into their respective index.
    for k in V:
        adjL[k[0]].append(k[1])
        adjL[k[1]].append(k[0])
    # returns adjacent list
    return adjL


def path(prev, origin):
    # Prints the path from our point of origin to our destination
    if prev[origin] != -1:
        path(prev, prev[origin])
    print(origin, ' - ', end=' ')

def breadth_First_search(G, origin):
    # Creates list if places we have visited
    visited = [False for i in range(len(G))]
    # Creates list of vertices which we have visited
    prev = [-1 for i in range(len(G))]
    # How we are going to traverse the graph
    queue = []
    # starting point
    queue.append(origin)
    # we have visited our starting point
    visited[origin] = True

    while len(queue) is not 0:
        # pop our starting point and move to vertices that have connections to our
        # current vertices
        u = queue.pop(0)
        for t in G[u]:
            if visited[t] is False:
                visited[t] = True
                prev[t] = u
                queue.append(t)
    return prev




def depthFirstSearchS(G, origin):
    # visited list
    visited = [False for i in range(len(G))]
    # previous list
    prev = [-1 for i in range(len(G))]
    # stack, way in which we are going tp traverse the graph
    stack = []
    stack.append(origin)
    visited[origin] = True

    while len(stack) is not 0:
        # pop our last item in the list and follow path until we have visited all
        # vertercies
        u = stack.pop()
        for t in G[u]:
            if visited[t] is False:
                visited[t] = True
                prev[t] = u
                stack.append(t)
    return prev


def depthFirstSearchR(G, origin):
    # traverse our graph as long we have items in our graph that we have not visited
    visited[origin] = True
    for t in G[origin]:
        if not visited[t]:
            prev[t] = origin
            depthFirstSearchR(G, t)
    return prev

plt.close("all")
# Creates Maze specs, x and y
maze_rows = 3
maze_cols = 3

walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)

#draw_maze(walls,maze_rows,maze_cols,cell_nums=True)

# User can choose which type of union to do, Standard, or compression
print('Which Disjoint set union do you want to apply:')
print('1. Standard Union')
print('2. Union by Size with path compression')
choice = int(input('Choice: '))

# Standard Union
if choice == 1:
    # Number of cells we have in our maze
    cells = maze_rows * maze_cols
    print('\nOur maze currently contains', cells, 'cells')
    print('\nHow many walls should be removed?')
    remWalls = int(input('Choice: '))

    # number of remove walls in less than 0
    if remWalls < 0:
        print('you cannot remove negative walls')
        exit(0)

    # number of removed walls is less than cells -1
    if remWalls <  cells-1:
        print('\nA path from source to destination is not guaranteed to exit\n')
        vertices = []
        # while we still have number of walls to be removed
        while remWalls != 0:
            # Select a random list and unionize them
            d = random.randint(0,len(walls)-1)
            if union(S,walls[d][0],walls[d][1]) != False:
                print('removing wall ',walls[d])
                # remove them from lists
                # add it to a vertices list
                vertices.append(walls[d])
                walls.pop(d)
                # decrease amount of remove walls
                remWalls -= 1
        # Final Disjoint Set, and maze drawing
        print('\nDisjoint Set: ',S)
        # Adjacent List
        adL = adjList(vertices, cells)
        print('\nAdjacent List: ',adL)
        # Searching path using Breadth_First_search
        print('Breadth_First_search: Staring Point: 0 | End Point:', cells-1)
        path(breadth_First_search(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        # Searching path using Depth First Search Recursive
        print('Depth First Search(Recursion): Starting Point: 0 | End Point:', cells-1)
        visited = [False for i in range(cells)]
        prev = [-1 for i in range(cells)]
        path(depthFirstSearchR(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        # Searching path using Depth First Search (Stacks)
        print('Depth First Search(Stack): Starting Point: 0 | End Point:', cells-1)
        path(depthFirstSearchS(adL,0),cells-1)
        print()
        # Draws maze
        draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
        plt.show()

    # When the number of remove walls is equal to number of cells -1
    if remWalls == cells-1:
        print('\nThere is a unique path from source to destination\n')
        vertices = []
        # While we have more than 1 set
        while remWalls != 0:
            # Select a random list and unionize them
            d = random.randint(0,len(walls)-1)
            if union(S,walls[d][0],walls[d][1]) != False:
                print('removing wall ',walls[d])
                # remove them from lists
                # add to lisd
                vertices.append(walls[d])
                walls.pop(d)
                remWalls -= 1
        # Final Disjoint Set, and maze drawing
        print('\nDisjoint Set: ',S)
        # Adjacent List
        adL = adjList(vertices, cells)
        print('\nAdjacent List: ',adL)
        #Breadth_First_search
        print('Breadth_First_search: Staring Point: 0 | End Point:', cells-1)
        path(breadth_First_search(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        # Depth First Search (Recursive)
        print('Depth First Search(Recursion): Starting Point: 0 | End Point:', cells-1)
        visited = [False for i in range(cells)]
        prev = [-1 for i in range(cells)]
        path(depthFirstSearchR(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        # Depth First Search (Stacks)
        print('Depth First Search(Stack): Starting Point: 0 | End Point:', cells-1)
        path(depthFirstSearchS(adL,0),cells-1)
        print()
        draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
        plt.show()

    # Number of remove walls is greater than cells-1
    if remWalls > cells-1:
        print('There is at least one path from source to destination')
        # if we have more walls to remove than the number of cells, set it to
        # the max amount of cells
        if remWalls > (maze_rows*(maze_rows-1))+(maze_cols*(maze_cols-1)):
            remWalls = (maze_rows*(maze_rows-1))+(maze_cols*(maze_cols-1))
        vertices = []
        # Keeps track of items we have removed
        count = 0
        # removes walls and adds them to their disjoint set
        while remWalls > 0:
            d = random.randint(0,len(walls)-1)
            # Select a random list and unionize them
            if union(S,walls[d][0],walls[d][1]) is not False:
                print('removing wall ',walls[d])
                vertices.append(walls[d])
                walls.pop(d)
                remWalls -= 1
                count += 1
            # once we reach our n point we will break, I did this becasue the loop
            # will go infinte times
            if count == cells-1:
                break
        # finish up the remaining walls, and add them to their sets
        while remWalls > 0:
            print('-')
            d = random.randint(0,len(walls)-1)
            print('removing wall ',walls[d])
            union(S,walls[d][0],walls[d][1])
            vertices.append(walls[d])
            walls.pop(d)
            remWalls -= 1
        # Final Disjoint Set, Breadth_First_search, depthFirstSearchR, depthFirstSearchS,
        print(vertices)
        print('\nDisjoint Set: ',S)
        adL = adjList(vertices, cells)
        print('\nAdjacent List: ',adL)
        print('Breadth_First_search: Staring Point: 0 | End Point:', cells-1)
        path(breadth_First_search(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Recursion): Starting Point: 0 | End Point:', cells-1)
        visited = [False for i in range(cells)]
        prev = [-1 for i in range(cells)]
        path(depthFirstSearchR(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Stack): Starting Point: 0 | End Point:', cells-1)
        path(depthFirstSearchS(adL,0),cells-1)
        print()
        draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
        plt.show()

# union by size and compression
if choice == 2:
    # number of cells
    cells = maze_rows * maze_cols
    print('\nOur maze currently contains', cells, 'cells')
    print('\nHow many walls should be removed?')
    remWalls = int(input('Choice: '))

    # if we remove negative number of cells
    if remWalls < 0:
        print('you cannot remove negative walls')
        exit(0)

    if remWalls <  cells-1:
        print('\nA path from source to destination is not guaranteed to exists\n')
        # stores vertices we have linked ot removed
        vertices = []

        while remWalls != 0:
            d = random.randint(0,len(walls)-1)
            # unionize items from random list
            if unionBySize(S,walls[d][0],walls[d][1]) != False:
                # remove from list
                print('removing wall ',walls[d])
                vertices.append(walls[d])
                walls.pop(d)
                remWalls -= 1
        # prints out information: Disjoint set, Breadth_First_search, depthFirstSearchR
        # depthFirstSearchS, and draws maze
        print('\nDisjoint Set: ',S)
        adL = adjList(vertices, cells)
        print('\nAdjacent List: ',adL)
        print('Breadth_First_search: Staring Point: 0 | End Point:', cells-1)
        path(breadth_First_search(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Recursion): Starting Point: 0 | End Point:', cells-1)
        visited = [False for i in range(cells)]
        prev = [-1 for i in range(cells)]
        path(depthFirstSearchR(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Stack): Starting Point: 0 | End Point:', cells-1)
        path(depthFirstSearchS(adL,0),cells-1)
        print()
        draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
        plt.show()

    # exactly one path per vertices
    if remWalls == cells-1:
        print('\nThere is a unique path from source to destination\n')
        vertices = []
        # stores walls we have removed
        while remWalls != 0:
            d = random.randint(0,len(walls)-1)
            # unionize items from random list
            if unionBySize(S,walls[d][0],walls[d][1]) != False:
                # remove from list
                print('removing wall ',walls[d])
                vertices.append(walls[d])
                walls.pop(d)
                remWalls -= 1
        # prints out information: Disjoint set, Breadth_First_search, depthFirstSearchR
        # depthFirstSearchS, and draws maze
        print('\nDisjoint Set: ',S)
        adL = adjList(vertices, cells)
        print('\nAdjacent List: ',adL)
        #graphs.draw_graph(adL)
        print('Breadth_First_search: Staring Point: 0 | End Point:', cells-1)
        path(breadth_First_search(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Recursion): Starting Point: 0 | End Point:', cells-1)
        visited = [False for i in range(cells)]
        prev = [-1 for i in range(cells)]
        path(depthFirstSearchR(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Stack): Starting Point: 0 | End Point:', cells-1)
        path(depthFirstSearchS(adL,0),cells-1)
        print()
        draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
        plt.show()

    if remWalls > cells-1:
        print('There is at least one path from source to destination')
        # While we have more than 1 set

        # if we remove more walls than the number of walls we have in our maze
        if remWalls > (maze_rows*(maze_rows-1))+(maze_cols*(maze_cols-1)):
            remWalls = (maze_rows*(maze_rows-1))+(maze_cols*(maze_cols-1))
        vertices = []
        # Stores removed walls
        count = 0
        # keeps count of when to break from loop
        while remWalls != 0:
            # Select a random list and unionize them
            d = random.randint(0,len(walls)-1)
            if unionBySize(S,walls[d][0],walls[d][1]) != False:
                print('removing wall ',walls[d])
                vertices.append(walls[d])
                walls.pop(d)
                remWalls -= 1
                count += 1
            # when we have n-1 walls removed, we will break from loop, otherwise
            # we will loop infinte times
            if count == cells -1:
                break
        # removes and adds remaining walls into their sets
        while remWalls != 0:
            d = random.randint(0,len(walls)-1)
            print('removing wall ',walls[d])
            unionBySize(S,walls[d][0],walls[d][1])
            vertices.append(walls[d])
            walls.pop(d)
            remWalls -= 1

        # prints out information: Disjoint set, Breadth_First_search, depthFirstSearchR
        # depthFirstSearchS, and draws maze
        print('\nDisjoint Set: ',S)
        adL = adjList(vertices, cells)
        print('\nAdjacent List: ',adL)
        print('Breadth_First_search: Staring Point: 0 | End Point:', cells-1)
        path(breadth_First_search(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Recursion): Starting Point: 0 | End Point:', cells-1)
        visited = [False for i in range(cells)]
        prev = [-1 for i in range(cells)]
        path(depthFirstSearchR(adL,0),cells-1)
        print()
        print('----------------------------------------------------------------')
        print('Depth First Search(Stack): Starting Point: 0 | End Point:', cells-1)
        path(depthFirstSearchS(adL,0),cells-1)
        print()
        draw_maze(walls,maze_rows,maze_cols,cell_nums=True)
        plt.show()

else:
    # User selects something else than 1 or 2
    exit(0)
