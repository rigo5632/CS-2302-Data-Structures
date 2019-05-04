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
    return ans

def backtracking_Partition(S,S1,last,goal):
    if goal == 0:
        return True,[],[]
    if goal < 0 or last < 0:
        return False,[],[]
    a, SS, S2= backtracking_Partition(S,S1,last-1,goal-S[last])
    if a:
        SS.append(S[last])
        S1[last] = 0
        S2 = []
        for i in range(len(S1)):
            if S1[i] != 0:
                S2.append(S1[i])
        return True, SS, S2
    else:
        return backtracking_Partition(S,S1,last-1,goal)

def checkDisjunction(S,S1,S2):
    if len(S1) < len(S2):
        for k in S1:
            if k in S2:
                return False
    else:
        for k in S2:
            if k in S1:
                return False
    return True

def checkUnion(S,S1,S2):
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

trigIdentities = ['sin(t)', 'cos(t)', 'tan(t)','1/cos(t)','-sin(t)', '-cos(t)'
, '-tan(t)', 'sin(-t)', 'cos(-t)', 'tan(-t)', '(sin(t))/(cos(t))', '(2) * (sin(t/2)) * (cos(t/2))'
, 'sin(t)*sin(t)', '1-((cos(t))*(cos(t)))', '(1-cos(t)*cos(t))/2', '1/(cos(t))']
comparisons = radomized_equal(trigIdentities)
print('Tirg Functions that equal each other:')
for i in range(len(comparisons)):
    for j in range(len(comparisons[i])):
        if comparisons[i][j]:
            print('[',trigIdentities[i],':', trigIdentities[j],']')
S = [2,4,5,9,12,2]
S1 = [S[i] for i in range(len(S))]
sum = 0
for i in range(len(S)):
    sum += S[i]
possibleSubset, subset1, subset2= (backtracking_Partition(S,S1,len(S)-1,sum/2))
S1 = 0
S2 = 0
if possibleSubset:
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
