# Author: Rigoberto Quiroz
# Section: 1:30 PM - 2:50 PM
# This Program will generate a linked list of random int elements then we will
# sort the list with various methods(Bubble sort, merge sort, quickSort, and
# a single recursion call quickSort). As we are sorting the linked list we will
# set a counter that will count how many comparisons that sorting will have.


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
    global count
    temp1 = L.head
    count = 0
    #Nested Loop, sorts each element one by one
    while temp1 is not None:
        temp = L.head
        #Comparison
        while temp.next is not None:
            count = count + 1
            if temp.item > temp.next.item:
                a = temp.item
                temp.item = temp.next.item
                temp.next.item = a
            temp = temp.next
        temp1 = temp1.next
    #returns sorted list
    return L


def quickSort(L):
    global count
    if Size(L) > 1:
        # Selects a pivot point
        pivot = L.head.item
        a = L.head.next
        L1 = List()
        L2 = List()

        while a is not None:
            count = count + 1
            # Sorts elements lower than pivot to left list and the rest to the right list
            if a.item <= pivot:
                Append(L1,a.item)
            else:
                Append(L2,a.item)
            a = a.next
        # Edits the list
        L1 = quickSort(L1)
        L2 = quickSort(L2)
        # Since we lose our pivot point, we have to re-add it
        Append(L1, pivot)
        # merge the to list
        return merge(L1,L2)
    else:
      return L

def merge(L1,L2):
    if IsEmpty(L1):
        return L2
    if IsEmpty(L2):
        return L1
    L1.tail.next = L2.head
    L1.tail = L2.tail
    return L1
def modQuickSort1(L):
    if Size(L)//2 == 1:
        return modQuickSort(L,Size(L))
    else: # even length
        return (modQuickSort(L, (Size(L) - 1) // 2))

def modQuickSort(L, K):
    global count
    if Size(L) > 1:
        # Selects a pivot point
        pivot = L.head.item
        a = L.head.next
        L1 = List()
        L2 = List()

        while a is not None:
            count = count + 1
            # Sorts elements lower than pivot to left list and the rest to the right list
            if a.item <= pivot:
                Append(L1,a.item)
            else:
                Append(L2,a.item)
            a = a.next

        if Size(L1) > K:
            return modQuickSort(L1,K)
        if Size(L1) == K:
            return pivot
        if Size(L1) < K:
            return modQuickSort(L2, K - Size(L1))
    else:
        return L
# Merge Sort
def mergeSort(L):
    if not IsEmpty(L) and L.head.next is not None:
        temp = L.head
        #Create two list, and split the original List in two halfs
        L1, L2 = splitList(L)
        L1 = mergeSort(L1)
        L2 = mergeSort(L2)
        sortedList = merge1(L1,L2)
        return sortedList
    else:
        return L

def merge1(L1, L2):
    global count
    sL = List()
    currentNode1 = L1.head
    currentNode2 = L2.head
    #Compares the two list items and depending on which item we add we will advance
    # to the next element of that list.
    while currentNode1 is not None and currentNode2 is not None:
        count = count + 1
        if currentNode1.item < currentNode2.item:
            Append(sL,currentNode1.item)
            currentNode1 = currentNode1.next
        else:
            Append(sL,currentNode2.item)
            currentNode2 = currentNode2.next
    #Get any elements that were left over.
    while currentNode1 is not None:
        Append(sL, currentNode1.item)
        currentNode1 = currentNode1.next

    while currentNode2 is not None:
        Append(sL, currentNode2.item)
        currentNode2 = currentNode2.next
    return sL

def splitList(L):
    temp = L.head
    L1 = List()
    L2 = List()
    n = 0
    # splits list into two halfs
    while n < Size(L)//2:
        Append(L1,temp.item)
        n = n + 1
        temp = temp.next
    while n < Size(L):
        Append(L2,temp.item)
        n = n + 1
        temp = temp.next
    return L1, L2

def Size(L):
    if L is None:
        return 0
    #Gets length of list
    temp = L.head
    count = 0
    while temp is not None:
        count = count + 1
        temp = temp.next
    return count

def Median(L):
    # gets the midpoint of list
    if Size(L) % 2 != 0:
        temp = L.head
        n = 0
        while n < Size(L) // 2:
            temp = temp.next
            n = n + 1
        return temp.item
    temp = L.head
    n = 0
    while n < Size(L)//2:
        temp = temp.next
        n = n + 1
    return temp.item

L = List()

for i in range(100):
    Append(L,random.randint(0,100))
count = 0
'''
print('Original List: ',end =' ')
Print(L)
print('Bubble Sorting: ', end = ' ')
Print(bubbleSort(L))
print('Median: ',end = ' ')
print(Median(bubbleSort(L)))
print('Count: ', count)
print('------------------------------------------')
'''
'''
count = 0
print('Original List: ',end =' ')
Print(L)
print('Merge Sorting: ', end = ' ')
Print(mergeSort(L))
print('Median: ',end = ' ')
print(Median(mergeSort(L)))
print('Count: ', count)

count = 0
print('------------------------------------------')
print('Original List: ',end =' ')
Print(L)
print('Quick Sorting: ', end = ' ')
Print(quickSort(L))
print('Median: ',end = ' ')
print(Median(quickSort(L)))
print('Count: ', count)

count = 0
print('------------------------------------------')
print('Original List: ',end =' ')
Print(L)
print('Quick Sorting(1 recursion Call): ', end = ' ')
Print(modQuickSort(L))
print('Median: ',end = ' ')
print(Median(modQuickSort(L)))
print('Count: ', count)
'''

print('------------------------------------------')
print('Original List: ',end =' ')
Print(L)
print('Quick Sorting(1 recursion Call): ', end = ' ')
print('\nMedian: ',end = ' ')
print(modQuickSort(L,Size(L)//2))
print('Count: ', count)
