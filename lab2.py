import random

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)

def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')

#List Functions
class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None

def IsEmpty(L):
    return L.head == None

def Append(L,x):
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print()

def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next

def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()

def bubbleSort(L):
    length = Size(L)
    n = 0
    while n < length:
        temp = L.head
        while temp.next is not None:
            if temp.item > temp.next.item:
                value = temp.item
                temp.item = temp.next.item
                temp.next.item = value
            temp = temp.next
        n = n + 1
    return L
def mergeSort(L):
    if Size(L) > 1:
        
def Size(L):
    temp = L.head
    count = 0
    while temp is not None:
        count = count + 1
        temp= temp.next
    return count

L = List()
'''
for i in range(5):
    Append(L,random.randint(0,200))
'''
Append(L,38)
Append(L,27)
Append(L,43)
Append(L,3)
Append(L,9)
Append(L,82)
Append(L,10)
Print(L)
#Print(bubbleSort(L))
mergeSort(L,Size(L))
