stack = []   # empty stack

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)






class Stack:
    def __init__(self, capacity):
        self.capacity = capacity      # max size of stack
        self.stack = [None] * capacity
        self.top = -1                 # empty stack

    # Push operation
    def push(self, value):
        if self.top == self.capacity - 1:
            print("Stack is FULL! Cannot push", value)
        else:
            self.top += 1
            self.stack[self.top] = value
            print(value, "pushed into stack")

    # Display stack
    def display(self):
        if self.top == -1:
            print("Stack is EMPTY!")
        else:
            print("Stack elements:", self.stack[:self.top+1])


# Example
s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
s.push(40)   # should say full
s.display()
