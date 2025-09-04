class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(value, "pushed")

    def pop(self):
        if self.top is None:
            print("Stack Underflow! Nothing to pop")
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data

    def isEmpty(self):
        return self.top is None


# Example
s = StackLinkedList()
s.push(5)
s.push(15)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Is Empty:", s.isEmpty())
