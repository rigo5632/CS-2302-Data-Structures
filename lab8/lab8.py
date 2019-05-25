# Author: Rigoberto Quiroz
# Section: 1:30 PM - 2:50 PM
# This program will get a list of trig functions, then we will compare them to see
# which are the same, they are the same then we will print them out otherwise
# we will skip it. We will check each function 1000 times with values between
# pi and - pi. For the second part we will enter a list of values, then the program
# will try to find a subset following the partition problem. If we do then we will
# print the subsets otherwise will print the error message displaying why there
# was no partition problem.

# libraries
import random
import numpy as np
from math import *

# randominzed algoritm
def radomized_equal(f,tries=1000,tolerance=0.0001):
    ans = [[] for i in range(len(f))]
    for i in range(len(f)):
        ans[i] = [True for i in range(len(f))]
    for i in range(len(f)):
        for j in range(len(f)):
            for x in range(tries):
                t = random.uniform(-pi, pi)
                f1 = eval(f[i])
                f2 = eval(f[j])
                if np.abs(f1-f2)>tolerance:
                    ans[i][j] = False
                    break
    # returns lists of same functions
    return ans

# Backtracking
def backtracking_Partition(S,S1,last,goal):
    # if we reach our goal
    if goal == 0:
        # return True and 2 empty lists
        return True,[],[]
    # otherwise return False and 2 empty lists (if we surpass our goal or index)
    if goal < 0 or last < 0:
        return False,[],[]
    # saves boolean and lists
    a, SS, S2= backtracking_Partition(S,S1,last-1,goal-S[last])
    if a:
        # if we have a true value we will append it to a list
        SS.append(S[last])
        S1[last] = 0
        S2 = []
        for i in range(len(S1)):
            if S1[i] != 0:
                S2.append(S1[i])
        # return Lists
        return True, SS, S2
    else:
        # goes back and checks other posiible lists
        return backtracking_Partition(S,S1,last-1,goal)


def checkDisjunction(S,S1,S2):
    # checks which is a subset of which
    if len(S1) < len(S2):
        # checks if we do not have repeated values
        for k in S1:
            if k in S2:
                return False
    else:
        for k in S2:
            if k in S1:
                return False
    return True

def checkUnion(S,S1,S2):
    # checks if all the values are still in the subsets
    if len(S1) + len(S2) != len(S):
        return False
    setSum = 0
    subsetSum = 0
    for k in S1:
        if k not in S:
            return False
    for k in S2:
        if k not in S:
            return False
    return True

# trig identites to compare
trigIdentities = ['sin(t)', 'cos(t)', 'tan(t)','1/cos(t)','-sin(t)', '-cos(t)'
, '-tan(t)', 'sin(-t)', 'cos(-t)', 'tan(-t)', '(sin(t))/(cos(t))', '(2) * (sin(t/2)) * (cos(t/2))'
, 'sin(t)*sin(t)', '1-((cos(t))*(cos(t)))', '(1-cos(t)*cos(t))/2', '1/(cos(t))']
comparisons = radomized_equal(trigIdentities)
# prints info
print('Tirg Functions that equal each other:')
for i in range(len(comparisons)):
    for j in range(len(comparisons[i])):
        if comparisons[i][j]:
            print('[',trigIdentities[i],':', trigIdentities[j],']')
# set to check
S = [2,4,5,9,12,2]
S1 = [S[i] for i in range(len(S))]
sum = 0
for i in range(len(S)):
    sum += S[i]
possibleSubset, subset1, subset2= (backtracking_Partition(S,S1,len(S)-1,sum/2))
S1 = 0
S2 = 0
if possibleSubset:
    # prints if we had a subsets or not
    union = checkUnion(S,subset1,subset2)
    disjunction = checkDisjunction(S,subset1,subset2)
    if union and disjunction:
        print('We have found subsets in Set =',S)
        print('Subset 1:', subset1)
        print('Subset 2:', subset2)
    else:
        if union is False:
            print('No set was found in Set =',S, 'becasue the Union of Subset1 and Subset2 are not subsets of S')
        else:
            print('No set was found in Set =',S, 'becasue the Disjuntion of Subset1 and Subset2 do not create an empty list')
            print('There is a value in common in Subset1 and Subset2')
else:
    print('No set was found in Set =',S)
