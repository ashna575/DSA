class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        new_node.prev = None

       
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

   
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

 
    def display_backward(self):
        temp = self.head

        while temp and temp.next:
            temp = temp.next
     
        while temp:
            print(temp.data, end=" <-> " if temp.prev else "")
            temp = temp.prev
        print()


# ----------------------------
# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(5)
dll.insert_at_beginning(4)
dll.insert_at_beginning(3)

print("Forward traversal:")
dll.display_forward()

print("Backward traversal:")
dll.display_backward()
