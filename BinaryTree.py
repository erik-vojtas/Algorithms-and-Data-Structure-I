# Binary Tree
# https://www.programiz.com/dsa/binary-tree

class Node:
    def __init__(self, data): # initiate Node
        self.left = None # left pointer
        self.right = None # right pointer
        self.data = data # data part

    def insert(self, data): # insert data into binary tree
        if self.data: # if self.data exists
            if data < self.data: # if inserted data < self.data
                if self.left is None: # if left pointer is None
                    self.left = Node(data) # then Node(inserted data) is assigned to left pointer
                else: # else
                    self.left.insert(data) # recursion
            elif data > self.data: # if inserted data > self.data
                if self.right is None: # if right pointer is None
                    self.right = Node(data) # then Node(inserted data) is assigned to right pointer
                else:
                    self.right.insert(data) # recursion
        else: # if self.data does not exist
            self.data = data # self.data = inserted data

    def printTree(self): # print Binary Tree
        if self.left: # if left pointer exists
            self.left.printTree() # recursion
        print(self.data) # print data
        if self.right: # if right pointer exists
            self.right.printTree() # recursion


rootNode = Node(5)
# rootNode.printTree()

rootNode.insert(4)
rootNode.insert(3)
rootNode.insert(7)
rootNode.insert(6)
rootNode.printTree()
print("----------------------------")

print(rootNode.data)