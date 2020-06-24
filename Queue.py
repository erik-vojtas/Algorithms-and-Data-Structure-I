# Queue Data Structure
# FIFO - first IN, first OUT

# class Queue:
#     def __init__(self):
#         self.queue = list()
#
#     def add2Q(self, value):
#         self.queue.insert(0, value)
#
#     def size(self):
#         return len(self.queue)
#
#     def getFromQ(self):
#         if len(self.queue) == 0:
#             print("No items left in queue")
#             return ""
#         else:
#             return self.queue.pop()
#
#     def pritQueue(self):
#         for x in self.queue:
#             print(x)
#
#
# MyQueue = Queue()
# MyQueue.add2Q("Plate1")
# MyQueue.add2Q("Plate2")
# MyQueue.add2Q("Plate3")
# MyQueue.add2Q("Plate4")
# MyQueue.add2Q("Plate5")
# MyQueue.add2Q("Plate6")
#
# MyQueue.pritQueue()
# print(MyQueue.size())
#
# print(MyQueue.getFromQ())


class Queue:
    def __init__(self, name):
        self.queue = list()
        self.name = name

    def printQueue(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            returnedStr = ""
            for item in self.queue:
                returnedStr += item + ", "
            print(returnedStr)

    def printFront(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            print("Top of the queue:", self.queue[-1])

    def printBack(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            print("Bottom of the queue:", self.queue[0])

    def __repr__(self):
        return self.name

    def pushIn(self, item):
        self.queue.insert(0, item)
        print(f"Item: {item} has been added to the queue.")

    def popOut(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            print(f"Item: {self.queue[-1]} has been removed.")
            self.queue.pop() # remove last item in list

    def popOutAndPushAllItemsToAnotherQueue(self, another_queue):
        if len(self.queue) == 0:
            print("Queue is empty!")
        else:
            for i in range(len(self.queue)-1, -1, -1):
                print(f"Item: {self.queue[i]} has been moved from {self.name} to {another_queue.name}.")
                another_queue.queue.insert(0, self.queue[i])
                self.queue.pop(i) # remove last item in list

myQueue1 = Queue("myQueue1")
myQueue1.pushIn("A")
myQueue1.pushIn("B")
myQueue1.pushIn("C")
myQueue1.pushIn("D")
myQueue1.pushIn("E")

myQueue1.printQueue()
myQueue1.printFront()
myQueue1.printBack()

myQueue2 = Queue("myQueue2")
myQueue1.popOutAndPushAllItemsToAnotherQueue(myQueue2)

myQueue2.printQueue()