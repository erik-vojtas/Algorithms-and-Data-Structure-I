#Stack Data Structure
# LIFO - last IN first OUT

class Stack:
    def __init__(self, name):
        self.name = name
        self.stack = []
        
    def printStack(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            returnedStr = ""
            for item in self.stack:
                returnedStr += item + ", "
            print(returnedStr)

    def printTop(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print("Top of the stack:", self.stack[-1])

    def printBottom(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print("Bottom of the stack:", self.stack[0])

    def __repr__(self):
        return self.name

    def pushIn(self, item):
        self.stack.append(item)
        print(f"Item: {item} has been added to the stack.")
    
    def popOut(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print(f"Item: {self.stack[-1]} has been removed.")
            self.stack.pop() # remove last item in list

    def popOutAndPushItemToAnotherStack(self, another_stack):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            print(f"Item: {self.stack[-1]} has been moved from {self.name} to {another_stack.name}.")
            another_stack.stack.append(self.stack[-1])
            self.stack.pop() # remove last item in list

    def popOutAndPushAllItemsToAnotherStack(self, another_stack):
        if len(self.stack) == 0:
            print("Stack is empty!")
        else:
            for i in range(len(self.stack)-1, -1, -1):
                print(f"Item: {self.stack[i]} has been moved from {self.name} to {another_stack.name}.")
                another_stack.stack.append(self.stack[i])
                self.stack.pop(i) # remove last item in list


myStack1 = Stack("myStack1")
myStack1.pushIn("A")
myStack1.pushIn("B")
myStack1.pushIn("C")
myStack1.pushIn("D")
myStack1.pushIn("E")

myStack1.printStack()
myStack1.printTop()
myStack1.printBottom()

myStack1.popOut()
myStack1.popOut()
myStack1.popOut()

myStack1.printStack()
myStack1.printTop()

myStack2 = Stack("myStack2")

myStack1.popOutAndPushAllItemsToAnotherStack(myStack2)

myStack1.printStack()
myStack2.printStack()
