stack = []   

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity      
        self.stack = [None] * capacity
        self.top = -1                 

    
    def push(self, value):
        if self.top == self.capacity - 1:
            print("Stack is FULL! Cannot push", value)
        else:
            self.top += 1
            self.stack[self.top] = value
            print(value, "pushed into stack")

   
    def display(self):
        if self.top == -1:
            print("Stack is EMPTY!")
        else:
            print("Stack elements:", self.stack[:self.top+1])



s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
s.push(40)   
s.display()
