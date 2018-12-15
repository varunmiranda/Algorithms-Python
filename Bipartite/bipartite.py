#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:30:39 2018

@author: varunmiranda
"""

"Reading the input file and converting it into an integer array format"

f = open("bipartite forest.txt")
lines = f.readlines()
text = [0]*(len(lines)-1)
graph = [[0 for i in range(2)] for j in range(len(lines)-1)]
string = ""

for i in range(1,len(lines)):
    text[i-1] = lines[i].splitlines()[0]
    for j in text[i-1]:
        if j == '(':
            continue
        elif j == ',':
            graph[i-1][0] = int(string)
            string = ""
        elif j == ')':
            graph[i-1][1] = int(string)
            string = ""
        else:
            string = string + j

"Storing the graph in an adjacency list"

key_arr = []

for i in range(0,len(lines)-1):
    for j in range(0,2):
        if(graph[i][j] not in key_arr):
            key_arr.append(graph[i][j])

adjacency = {}

for i in key_arr:
    for j in range(0,len(lines)-1):
       if graph[j][0] == i:
           if i not in adjacency.keys():
               adjacency.setdefault(i, [])
           adjacency[i].append(graph[j][1])
               
       elif graph[j][1] == i:
           if i not in adjacency.keys():
               adjacency.setdefault(i, [])
           adjacency[i].append(graph[j][0])

string = ""

for i in range(0,len(lines[0])):
    if lines[0][i] != '\n':
        string = string + lines[0][i]

n = int(string)

for i in range(1,n+1):
    if i not in adjacency.keys():
        adjacency.setdefault(i,[])
           
"Coloring of the nodes using DFS by traversing the adjacency list"

node = min(adjacency.keys())
color = []

color.append({})
k=0
color[k].setdefault(node, ["red"])

def coloring(node):
    if color[k][node][0] == "red":
        for i in adjacency[node]:
            if i not in color[k].keys():
                color[k].setdefault(i, ["blue"])          
                coloring(i)
            elif i in color[k].keys() and "red" in color[k][i] and "blue" not in color[k][i]:
                color[k][i].append("blue")
                coloring(i)
    else:
        for i in adjacency[node]:
            if i not in color[k].keys():
                color[k].setdefault(i, ["red"])
                coloring(i)
            elif i in color[k].keys() and "blue" in color[k][i] and "red" not in color[k][i]:
                color[k][i].append("red")
                coloring(i)
    return color[k]

coloring(node)
visited = []
for i in color[k].keys():
    visited.append(i)

"Bipartite check"

red_array = []
blue_array = []
message = "Bipartite"

def bipartite(color):
    for i in color.keys():
        if len(color[i]) > 1:
            message = "Not bipartite"
            return message
        else:
            if color[i][0] == 'red':
                red_array.append(i)
            else:
                blue_array.append(i)

message = bipartite(color[k])

for i in key_arr:
    if i not in visited:
        k = k+1
        color.append({})
        color[k].setdefault(i, ["red"])
        coloring(i)
        bipartite(color[k])
        for i in color[k].keys():
            visited.append(i)

if message == "Not bipartite":
    print (message)
else:
    print ("Bipartite")
    for i in range(1,n):
        if i not in red_array and i not in blue_array:
            red_array.append(i)
    print ("First set", red_array)
    print ("Second set", blue_array)

