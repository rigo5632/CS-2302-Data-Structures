# Author: Rigoberto Quiroz
# Section: 1:30 PM - 2:50 PM
# This program will create a Hash table and a BST(Binary Search Tree) and will
# insert data from a file called glove.6B.50d.txt (word and embeddings), into
# these data structures. We will compute varies things such as height of BST,
# Number of nodes, pecentage of empty lists, etc. Once all of these fields have
# been computed we will search for words and their similarities. We will output
# how similary these two words are, the closer to 1, the more similar, the
# closer to -1 the less similar.

import numpy as np
import math
import time

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        # self.item holds an array contaning a word and its embeddings
        self.item = item
        self.left = left
        self.right = right

def Insert(T,newItem, l):
    # If we find an empty stop in our bst we will add the word and embeddings
    if T == None:
        T =  BST([newItem, l])
    # Information is organzied in alphabetical order.
    elif T.item[0] > newItem:
        T.left = Insert(T.left,newItem, l)
    else:
        T.right = Insert(T.right,newItem, l)
    return T

def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.word, T.embeding, end = ' ')
        InOrder(T.right)

def totalNodes(T):
    if T is None:
        return 0
    if T is not None:
        # adds 1 for each node we find in our bst
        nodeCounter = 1 + totalNodes(T.left) + totalNodes(T.right)
        return nodeCounter

def height(T):
    if T is None:
        return 0
    leftBranch = 1+height(T.left)
    rightBranch = 1+height(T.right)
    # returns the height of bst
    if leftBranch > rightBranch:
        return leftBranch
    return rightBranch

def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        print(space,T.word)
        InOrderD(T.right,space+'   ')
        InOrderD(T.left,space+'   ')

def findEmb(T, k):
    if T is None:
        return None
    # We found the word we are looking for, returning its embedding
    if T.item[0] == k:
        return T.item[1]
    # Move left if the word comes first than the word we are currently are
    if T.item[0] > k:
        return findEmb(T.left,k)
    # moves right otherwise
    return findEmb(T.right,k)

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):
        self.item = []
        for i in range(size):
            self.item.append([])
        # keeps record on how many items our hashTable has
        self.num_Items = 0

def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list)
    # Does nothing if k is already in the table
    H.num_Items += 1
    # Locates the location where the information will be placed
    b = h(k,len(H.item))
    # if load factor reaches 1 or a greater value
    if H.num_Items / len(H.item) >= 1.0:
        # adds more space into our hash table
        for i in range(len(H.item)+1):
            H.item.append([])
        # re-finds a location according to the new information about the hash
        b = h(k,len(H.item))
    # adds to hash
    H.item[b].append([k,l])

def FindC(H,k):
    # Returns bucket (b) and index (i)
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        # word found, returning embedding
        if H.item[b][i][0] == k:
            return H.item[b][i][1]
    return None
# equation for inserting items into our hash table
def h(s,n):
    r = 0
    for c in s:
        r = (r*27 + ord(c))%n
    return r

def loadFactor(H):
    if H is None:
        return None
    count = 0
    # counts how many items we have in our hash table
    for i in range(len(H.item)):
        count += len(H.item[i])
    # returns its load factor
    return count/len(H.item)

def emptyPercentage(H):
    if H is None:
        return None
    # checks how many emty list we have in our hash table
    empty = 0
    for i in range(len(H.item)):
        if len(H.item[i]) == 0:
            empty += 1
    # computes percentage and returns it
    percentage = (empty * 100) / len(H.item)
    return percentage


def average(H):
    if H is None:
        return None
    lengths = 0
    # computes the average of the length of list in our hashTable
    for i in range(len(H.item)):
        lengths += len(H.item[i])
    return lengths / len(H.item)

def standardDeviation(H):
    if H is None:
        return None
    # Computes Standard deviation by:
    # Getting Average --> subtracting the mean and then squaring it -->
    # adding all the values from previous steps --> multiplies the total sum by
    # 1/number of items we added --> squaring the final result and returns it
    avg = average(H)
    a = []
    for i in range(len(H.item)):
        if len(H.item[i]) >= 1:
            value = math.pow((len(H.item[i]) - avg),2)
            a.append(value)
    count = 0;
    for j in range(len(a)):
        count += a[j]
    value2 = count*(1/len(H.item))
    final = math.sqrt(value2)
    return final


# name of file
file = 'glove.6B.50d.txt'
# User has options, which data structure they wanna use
print('Choose Table implementation:')
print('1. Hash Table with Chaining: [Enter 1]')
print('2. Binary Tree: [Enter 2]')
choice = int(input('Choice: '))

# Hash Table Process
if choice == 1:
    print()
    #Builds hash table
    print('Building Hash Table with Chaining...\n')
    hashStart = time.time()
    H = HashTableC(11)
    originalSize = len(H.item)
    f = open(file, encoding='utf8')
    content = []
    embedding = np.arange(50)
    for x in f:
        content = x.split(' ')
        if ord(content[0][0]) >= 65 and ord(content[0][0]) <= 90 or ord(content[0][0]) >= 97 and ord(content[0][0]) <= 122:
            word = content[0]
            embedding = content[1:]
            InsertC(H,word, embedding)
    # Re-computes hashtable to set all keys in there correct positions
    print('Checking hash table...')
    print()
    count = 0
    H1 = HashTableC(len(H.item))
    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
            InsertC(H1,H.item[i][j][0],H.item[i][j][1])
    print('Hash Table Stats:')
    print('Initail Table Size:', originalSize)
    print('Final Table Size:', len(H1.item))
    print('Load Factor:', loadFactor(H1))
    print('Percentage of empty lists: %', emptyPercentage(H1))
    print('Standard deviation of lengths of the list:', standardDeviation(H1))
    print()
    print('Reading word file to determine similarities')
    print()
    print('Word similarities found:')
    # open file with words to compare
    file = open('myfile.txt', 'r')
    for x in file:
        dotProduct = 0
        magnitudude1 = 0
        magnitudude2 = 0
        comp = x.split()
        w1 = comp[0]
        w2 = comp[1]
        # finds words and gets their embedding
        # if we do not find the word then we will break from loop
        w1Embedding = FindC(H1,w1)
        if w1Embedding is None:
            print(w1,'not found.')
        w2Embedding = FindC(H1,w2)
        if w2Embedding is None:
            print(w2,'not found')
        # Computes how similar the words are
        if w2Embedding != None and w1Embedding != None:
            for i in range(len(w1Embedding)):
                dotProduct += float(w1Embedding[i]) * float(w2Embedding[i])
                magnitudude1 += math.pow(float(w1Embedding[i]),2)
                magnitudude2 += math.pow(float(w2Embedding[i]),2)
            totalMag = math.sqrt(magnitudude1 * magnitudude2)
            # prints the info of words
            print('Similatities [', w1, w2, '] = ', round((dotProduct/totalMag),4))
    hashEnd = time.time()
    print('Running time for hash table query processing:', hashEnd - hashStart)

elif choice == 2:
    totalStart = time.time()
    print()
    # Builds BST
    print('Building Binary Search Tree Tree...\n')
    T = None
    f = open(file, encoding='utf8')
    embedding = np.arange(50)
    startTime = time.time()
    for x in f:
        content = x.split(' ')
        if ord(content[0][0]) >= 65 and ord(content[0][0]) <= 90 or ord(content[0][0]) >= 97 and ord(content[0][0]) <= 122:
            word = content[0]
            embedding = content[1:]
            T = Insert(T,word, embedding)
    f.close()
    endTime = time.time()
    print('Binary Search Tree Stats:')
    print('Number of Nodes:', totalNodes(T))
    print('Height:', height(T))
    print('Running time for Binary Search Tree Construction:', endTime - startTime)
    print()
    print('Reading word file to determine similatities')
    print()
    print('Word similatities found:')
    # Reads file to see the word similarities
    file = open('myfile.txt', 'r')
    for x in file:
        dotProduct = 0
        magnitudude1 = 0
        magnitudude2 = 0
        comp = x.split()
        w1 = comp[0]
        w2 = comp[1]
        # Looks for the word and gets their embeddings
        # if we do not find the word we will break from loop
        w1Embedding = findEmb(T,w1)
        if w1Embedding is None:
            print(w1,'not found.')
        w2Embedding = findEmb(T,w2)
        if w2Embedding is None:
            print(w2,'not found')
        # Computes similarities
        if w1Embedding != None and w2Embedding != None:
            for i in range(len(w1Embedding)):
                dotProduct += float(w1Embedding[i]) * float(w2Embedding[i])
                magnitudude1 += math.pow(float(w1Embedding[i]),2)
                magnitudude2 += math.pow(float(w2Embedding[i]),2)
            totalMag = math.sqrt(magnitudude1 * magnitudude2)
            print('Similatities [', w1, w2, '] = ', round((dotProduct/totalMag),4))
    totalEnd = time.time()
    print()
    print('Running time for binary search tree query processing: ', totalEnd - totalStart)

else:
    # if user selects something other than Hash table or BST
    print('invalid input')
