#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:01:03 2018

@author: varunmiranda

Citations:
https://stackoverflow.com/questions/21522234/how-to-get-all-unique-characters-in-a-textfile-unix-python
https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
Introduction to Algorithms 3rd Edition, CLRS - Huffman coding implementation
"""

import os
import heapq

"Step 1: Reading the input text file"

os.chdir('/Users/varunmiranda/Desktop/IUB/Courses/Applied Algorithms/Programming Assignment 5')
text_file = open('source_text.txt','r').read()

"Step 2: Coverting all text to lower case and allowing only 32 characters"

text_file = text_file.lower()

def replaceMultiple(mainString, toBeReplaces, newString):
    for elem in toBeReplaces :
        if elem in mainString :
            mainString = mainString.replace(elem, newString)
    return  mainString

numbers = ['0','1','2','3','4','5','6','7','8','9']
escape_sequences = ['\n','\r','\xaa','\xbb','\xbf','\xc3','\xef']
other_characters = ['"','#','$','%','(',')','*','-','/',':',';','@','[',']','_']

forbidden_characters = numbers+escape_sequences+other_characters
text_file = replaceMultiple(text_file,forbidden_characters,"")

unique_chars = set(text_file)

"Step 3: Calculating the frequency of each character in the new text file"

def frequency(string):
    dictionary = {}
    for freq in string:
        char = dictionary.keys()
        if freq in char:
            dictionary[freq] += 1
        else:
            dictionary[freq] = 1
    return dictionary

letter_count = frequency(text_file)

"Step 4: Creating the huffman tree"

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

Q = []					
for c in letter_count:
    f = letter_count[c]	
    my_node = Node(c,f)		
    my_node.char = c
    my_node.freq = f	
    heapq.heappush(Q, (letter_count[c], my_node))

def huffman(letter_count):
    
    n = len(letter_count)
    for i in range(0,n-1):
        
        z = Node()
        
        x = heapq.heappop(Q)[1]
        z.left = x

        y = heapq.heappop(Q)[1]
        z.right = y
        
        z.freq = x.freq+y.freq
        
        heapq.heappush(Q, (z.freq, z))
        
    return heapq.heappop(Q)[1]
        
root_node = huffman(letter_count)

"Step 5: Traversing through the tree and assigning bits to characters"

array = {}
def traverseTree(node, bit):
    if node.left is None and node.right is None:	
         print node.char, bit
         array[node.char] = len(bit)
         
    else:
		traverseTree(node.left, bit + '0')	
		traverseTree(node.right, bit + '1')	
    return array

solution = traverseTree(root_node, '')

number_of_bits = 0
for character in letter_count:
    number_of_bits = number_of_bits + solution[character]*letter_count[character]

"Step 6: Discussion and comparisons with fixed length encoding"

length = len(text_file)

print "\nThe text was encoded using",number_of_bits,"bits"
print "The text had",length,"valid characters"
print "Using a 5-bit fixed length encoding, this would have been", length*5,"bits long"
print "So we saved",(length*5)-number_of_bits,"bits!"