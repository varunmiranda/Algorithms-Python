#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: varunmiranda

Citation:
Introduction to Algorithms 3rd Edition, CLRS - LCS implementation (Dynamic Programming)

"""

"Reading the Inputs"

X=['A','B','C','B','D','A','B']
Y=['B','D','C','A','B','A']

#X=[1, 0, 0, 1, 0, 1, 0, 1] 
#Y=[0, 1, 0, 1, 1, 0, 1, 1, 0]

m=len(X)
n=len(Y)

"Initializing b and c that stores the directions and the values respectively"

b = [[' ' for i in range(n)] for j in range(m)]
c = [[0 for i in range(n+1)] for j in range(m+1)]

"Setting the first row and first column as 0 in array c"

for i in range(1,m+1):
    c[i][0] = 0
for j in range(0,n+1):
    c[0][j] = 0

"tl denotes top left, t denotes top, l denotes left"

for i in range(1,m+1):
    for j in range(1,n+1):
        if(X[i-1]==Y[j-1]):
            c[i][j] = c[i-1][j-1]+1
            b[i-1][j-1] = "tl"
        elif(c[i-1][j] >= c[i][j-1]):
            c[i][j] = c[i-1][j]
            b[i-1][j-1] = "t"
        else:
            c[i][j] = c[i][j-1]
            b[i-1][j-1] = "l"

"Storing the longest common subsequence in an array Z"

def print_lcs(b,X,i,j):
    if i==-1 or j==-1:
        return Z
    if b[i][j] == "tl":
        print_lcs(b,X,i-1,j-1)
        Z.append(X[i])
    elif b[i][j] == "t":
        print_lcs(b,X,i-1,j)
    else:
        print_lcs(b,X,i,j-1)

"Providing the initial parameters for the print_lcs function and returning Z"

Z = []
print_lcs(b,X,m-1,n-1)
print(Z)
