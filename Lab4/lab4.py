# Author: Rigoberto Quiroz
# Section: 1:30PM - 2:50 PM
# This program will create a B-Tree(Balance Tree), and will display the height
# of the tree. It will extract the elements in ascsending order into a native
# list. It will find the max in the min node at a given depth. It will also
# output the total number of nodes in the B-Tree, the Nodes that are full
# (5 elements). Print all the items at a given depth and finally and find a given
# and return the output

import time

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):
        self.item = item
        self.child = child
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)

def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m)
            T.child[k] = l
            T.child.insert(k+1,r)
            k = FindChild(T,i)
        InsertInternal(T.child[k],i)

def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid])
        rightChild = BTree(T.item[mid+1:])
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf)
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf)
    return T.item[mid], leftChild,  rightChild

def InsertLeaf(T,i):
    T.item.append(i)
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)
        InsertInternal(T.child[k],i)


def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])


def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)

def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])

def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')

def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)

def extract(T,sL):
    if T.isLeaf:
        for i in range(len(T.item)):
            # appends single elements into list
            sL.append(T.item[i])
        return
    for i in range(len(T.item)):
        extract(T.child[i],sL)
        # appends the leftmost element then continues to the middle and so on
        sL.append(T.item[i])
    # goes to the right section of the tree
    extract(T.child[len(T.item)],sL)
    return sL

def minAtDepth(T,depth):
    # BST is empty
    if len(T.item) <= 0:
        return None
    # min element from the leftmost list
    if depth == 0:
        return T.item[0]
    # if depth exceeds B-Tree depth
    if T.isLeaf:
        return None
    # moves left to find the the min value
    return minAtDepth(T.child[0],depth-1)

def maxAtDepth(T,depth):
    #BST is empty
    if len(T.item) <= 0:
        return None
    # max element found
    if depth == 0:
        return T.item[len(T.item)-1]
    # depth exceeds B-Tree depth
    if T.isLeaf:
        return None
    # moves right
    return maxAtDepth(T.child[len(T.item)],depth-1)

def totalAtDepth(T, depth):
    #BST is empty
    if len(T.item) <= 0:
        return None
    # number of elements at depth
    if depth == 0:
        return 1
    # if depth exceeds B-Tree depth
    if T.isLeaf:
        return 0
    count = 0
    # records left and right branches
    for i in range(len(T.item)):
        count += totalAtDepth(T.child[i],depth-1)
    count += totalAtDepth(T.child[len(T.item)],depth-1)
    return count

def itemsAtDepth(T,depth):
    if len(T.item) <= 0:
        return None
    # prints elements at depth
    if depth == 0:
        print(T.item)
        return
    # if depth exceeds B-Tree depth
    if T.isLeaf:
        return None
    # moves left and right
    for i in range(len(T.item)):
        itemsAtDepth(T.child[i],depth-1)
    itemsAtDepth(T.child[len(T.item)],depth-1)

def fullNodes(T):
    if len(T.item) <= 0:
        return None
    # if list is full we add 1
    if len(T.item) == T.max_items:
        return 1
    # reaching leaves
    if T.isLeaf:
        return 0
    count = 0
    # B-Tree traversal
    for i in range(len(T.item)):
        count += fullNodes(T.child[i])
    count += fullNodes(T.child[len(T.item)])
    return count

def fullLeafNodes(T):
    if len(T.item) <= 0:
        return None
    # when we reach leafs we check which leaf list are full
    if T.isLeaf:
        if len(T.item) == T.max_items:
            return 1
        else:
            return 0
    count = 0
    # B-Tree traversal
    for i in range(len(T.item)):
        count += fullLeafNodes(T.child[i])
    count += fullLeafNodes(T.child[len(T.item)])
    return count

def keyAtDepth(T, key,h):
    if len(T.item) <= 0:
        return None
    for i in range(len(T.item)):
        # Key Found
        if T.item[i] == key:
            return 0
        if T.item[i] > key:
            return 1 + keyAtDepth(T.child[i],key,h)
    # key not found in B-Tree
    if T.isLeaf:
        return -(h+1)
    return 1 + keyAtDepth(T.child[len(T.item)],key,h)

L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
#L = []
T = BTree()
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'')
    #Print(T)
    print('\n####################################')

TotalTimeStart = time.time()
print('B-Tree Information:')
#--------------------------------------------------------------
print('--------------------------------------------------------')
startTime = time.time()
print('Height of Tree: ',height(T))
endTime = time.time()
print('Height Time:', endTime - startTime, 'seconds')
print('--------------------------------------------------------')
#--------------------------------------------------------------
h = height(T)
a = extract(T,[])
#-------------------------------------------------------------
startTime = time.time()
print('Extracted elements from list:', a)
endTime = time.time()
print('Extraction Time:', endTime - startTime, 'seconds')
print('--------------------------------------------------------')
#-------------------------------------------------------------
startTime = time.time()
print('Min at depth: ',minAtDepth(T,2))
endTime = time.time()
print('Min Element Time:', endTime - startTime, 'seconds')
print('--------------------------------------------------------')
#-------------------------------------------------------------
startTime = time.time()
print('Max at depth:', maxAtDepth(T,2))
endTime = time.time()
print('Max Element Time:', endTime - startTime, 'seconds')
print('--------------------------------------------------------')
#-------------------------------------------------------------
startTime = time.time()
print('Number of nodes at depth:', totalAtDepth(T,2))
endTime = time.time()
print('Number of Nodes Time:', endTime - startTime, 'seconds')
print('--------------------------------------------------------')
#-------------------------------------------------------------
startTime = time.time()
print('Items at depth: ')
itemsAtDepth(T,2)
endTime = time.time()
print('Elements at Depth Time:', endTime - startTime, 'seconds')
print()
print('--------------------------------------------------------')
#-------------------------------------------------------------
startTime = time.time()
print('Nodes that are full:', fullNodes(T))
endTime = time.time()
print('Full Nodes Time:', endTime - startTime, 'seconds')
print('--------------------------------------------------------')
#-------------------------------------------------------------
startTime = time.time()
print('Leave nodes that are full:',  fullLeafNodes(T))
endTime = time.time()
print('Full leave Nodes Time:', endTime - startTime, 'seconds')
print('--------------------------------------------------------')
#-------------------------------------------------------------
if a is None:
    print('Tree is empty')
else:
    startTime = time.time()
    for i in range(len(a)):
        print('Looking for ', a[i], end=' ')
        print('Depth: ',keyAtDepth(T,a[i],h))
        endTime = time.time()
    print('Search Key Time:', endTime - startTime, 'seconds')
    print('--------------------------------------------------------')
#-------------------------------------------------------------
TotalTimeEnd = time.time()
print('Total Program Time:', TotalTimeEnd - TotalTimeStart, 'seconds')
