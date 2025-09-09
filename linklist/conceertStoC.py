class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

# Link nodes (SLL)
n1.next = n2
n2.next = n3
n3.next = n4

# Head pointer
head = n1

# --- Convert to Circular Linked List ---
current = head
while current.next is not None:   # go to last node
    current = current.next

current.next = head   # last node points to head

# --- Traverse CLL (print only limited nodes to avoid infinite loop) ---
print("Circular Linked List Traversal:")
current = head
count = 0
while count < 8:   # print 8 steps to show the circular nature
    print(current.data, end=" -> ")
    current = current.next
    count += 1

print("...")
