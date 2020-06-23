
class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Single Linked List is empty!")
        else:
            tempStr = ""
            while self.head != None:
                tempStr += f"{self.head.value}, "
                self.head = self.head.nextNode
            returnedStr = tempStr[:-2]
            print(f"[{returnedStr}]")

    def __repr__(self):
        tempStr = ""
        while self.head != None:
            tempStr += f"{self.head.value}, "
            self.head = self.head.nextNode
        returnedStr = tempStr[:-2]
        return f"[{returnedStr}]"

    def insertValueAtBegin(self, new_value):
        new_node = Node(new_value)
        self.head, new_node.nextNode = new_node, self.head

    def insertNodeAtBegin(self, new_node):
        self.head, new_node.nextNode = new_node, self.head

    def insertValueAtEnd(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.nextNode is not None:
            last_node = last_node.nextNode
        last_node = new_node

    def insertNodeAtEnd(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.nextNode:
            last_node = last_node.nextNode
        last_node.nextNode = new_node

    def insertNodeAtNode(self, node, new_node):
        if node is None:
            print(f"Node does not exist!")
            return
        else:
            new_node.nextNode = node.nextNode
            node.nextNode = new_node

    def removeNode(self, node2remove):
        if node2remove is None:
            print(f"Node does not exist!")
            return
        node = self.head
        while node:
            if node.nextNode == node2remove:
                node.nextNode = node2remove.nextNode
                return
            elif node == node2remove:
                node.nextNode = node2remove.nextNode
                return
            node = node.nextNode


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

list_of_nodes = [n1,n2,n3,n4,n5]

myList = SingleLinkedList()

for node in list_of_nodes:
    myList.insertNodeAtEnd(node)

print(myList)
print("-----------------------------")

mySL = SingleLinkedList()
nodeA = Node("A")
mySL.head = nodeA

nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

mySL.head.nextNode = nodeB
nodeB.nextNode = nodeC

# mySL.insertNodeAtNode(nodeB, nodeD)
# mySL.printList()
print("-----------------------------")
#
mySL.removeNode(nodeB)
mySL.printList()