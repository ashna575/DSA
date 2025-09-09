class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

# Link nodes
n1.next = n2
n2.next = n3
n3.next = n4

# Head pointer
head = n1

# --- Reverse the linked list ---
prev = None
current = head

while current is not None:
    next_node = current.next   # store next node
    current.next = prev        # reverse the link
    prev = current             # move prev forward
    current = next_node        # move current forward

head = prev   # update head to new first node

# --- Traverse and print reversed list ---
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")
