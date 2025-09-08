class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


node1=Node(10)
node2=Node(33)
node3=Node(34)
node4=Node(89)

node1.next=node2
node2.next=node3
node3.next=node4

key=int(input("enter key value:"))
head=node1
current=head
while current.next.data != key:
    current=current.next
current.next=current.next.next    

current=head
while current is not None:
    print(current.data,end="=>")
    current=current.next