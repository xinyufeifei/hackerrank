#!/bin/python3

import os
import sys
from collections import deque
sys.setrecursionlimit(15000)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return '<{0}, {1}, {2}>'.format(self.data, self.left, self.right)

def construct_tree(indexes):
    tree = Node(1)
    fringe = deque([tree])
    current_layer_nodes = 1
    current_index = 0
    while current_index < len(indexes):
        next_layer = indexes[current_index:current_index + current_layer_nodes]
        for L, R in next_layer:
            head = fringe.popleft()
            if L != -1:
                head.left = Node(L)
                fringe.append(head.left)
            if R != -1:
                head.right = Node(R)
                fringe.append(head.right)
        current_index += current_layer_nodes
        current_layer_nodes = sum([1 for item in next_layer for i in item if i != -1])
        #print(tree)
    return tree

def swapEveryKLevelUtil(root, level, k): 
      
    # Base Case  
    if (root is None or (root.left is None and
                        root.right is None ) ): 
        return 
    # If current level+1 is present in swap vector 
    # then we swap left and right node 
    if level%k == 0: 
        root.left, root.right = root.right, root.left 
      
    # Recur for left and right subtree 
    swapEveryKLevelUtil(root.left, level+1, k) 
    swapEveryKLevelUtil(root.right, level+1, k)

def swapEveryKLevel(root, k): 
      
    # Call swapEveryKLevelUtil function with  
    # initial level as 1 
    swapEveryKLevelUtil(root, 1, k)

# Method to find the inorder tree travesal 
def inorder(root, visited_nodes): 
      
    # Base Case
    if root is None: 
        return
    inorder(root.left, visited_nodes)
    visited_nodes.append(root.data)
    inorder(root.right, visited_nodes)
    return visited_nodes
        

def swapNodes(indexes, queries):
    # construct the tree
    tree = construct_tree(indexes)
    result = []
    for k in queries:
        swapEveryKLevel(tree, k)
        #print(tree)
        visited_nodes = inorder(tree, [])
        #print(visited_nodes)
        result.append(visited_nodes)
    return result

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
