#DoublyLinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None
        self.previous_value = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self): # display all item in the doubly linked list
        if self.head is None and self.tail is None:
            print("Doubly linked list is empty.")
        printed_value = self.head
        while printed_value:
            print(printed_value.value)
            printed_value = printed_value.next_value

    def insertAtStart(self, new_node): # insert a node with value at the start of the doubly linked list
        if self.head is None:   # if the doubly linked list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.insertBeforeNode(self.head, new_node)

    def insertAtEnd(self, new_node): # insert a node with value at the end of the doubly linked list
        if self.tail is None:   # if the doubly linked list is empty
            self.tail = new_node
            self.head = new_node
        else:
            self.insertAfterNode(self.tail, new_node)

    def insertAfterNode(self, node, new_node): # insert a node after a certain node
        new_node.previous_value = node
        if node.next_value is None: # if node does not have next value then
            self.tail = new_node    # new node is the last node in the doubly linked list
        else:
            new_node.next_value = node.next_value
            new_node.next_value.previous_value = new_node
        node.next_value = new_node

    def insertBeforeNode(self, node, new_node): # insert a node before a certain node
        new_node.next_value = node
        if node.previous_value is None: # if node does not have previous value then
            self.head = new_node        # new node is the first node in the doubly linked list
        else:
            new_node.previous_value = node.previous_value
            new_node.previous_value.next_value = new_node
        node.previous_value = new_node

    def removeNode(self, node): # remove a node
        if node.previous_value is None: # if node does not have previous value then
            self.head = node.next_value
        else:
            node.previous_value.next_value = node.next_value
        if node.next_value is None:     # if node does not have next value then
            self.tail = node.previous_value
        else:
            node.next_value.previous_value = node.previous_value

    def removeAllNodes(self):  # remove all items in the doubly linked list
        self.head = None
        self.tail = None

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

my_dl = DoublyLinkedList()

#Insert at End
my_dl.insertAtEnd(nodeD)
my_dl.printList()
print("---------------------")

#Insert at Start
my_dl.insertAtStart(nodeA)
my_dl.printList()
print("---------------------")

#Insert at End
my_dl.insertAtEnd(nodeE)
my_dl.printList()
print("---------------------")

#Insert after nodeA
my_dl.insertAfterNode(nodeA, nodeB)
my_dl.printList()
print("---------------------")

#Insert before nodeD
my_dl.insertBeforeNode(nodeD, nodeC)
my_dl.printList()
print("---------------------")

#Remove node - last
my_dl.removeNode(nodeE)
my_dl.printList()
print("---------------------")

#Remove node - first
my_dl.removeNode(nodeA)
my_dl.printList()
print("---------------------")

#Remove all nodes
my_dl.removeAllNodes()
my_dl.printList()


