class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(n1):
    prev = None
    current = n1

    while current is not None:
        nxt = current.next  
        current.next = prev     
        prev = current          
        current = nxt           

    return prev 


def print_list(head):
    current = head
    while current :
        print(current.data, end=" -> ")
        current = current.next
    print("None")



n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

print("Original Linked List:")
print_list(n1)


reversed_head = reverse(n1)
print("Reversed Linked List:")
print_list(reversed_head)
