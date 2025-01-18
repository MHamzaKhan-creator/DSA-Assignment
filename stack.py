class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack is empty"
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.top is None:
            return "Stack is empty"
        return self.top.data

    def is_empty(self):
        return self.top is None


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  
print(stack.peek()) 
