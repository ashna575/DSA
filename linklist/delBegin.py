class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(10)
n2=Node(84) 
n3=Node(87)
n4=Node(90)


n1.next=n2
n2.next=n3
n3.next=n4

head=n1
if head is not None:
    head=head.next

current=head
while current is not None:
   print(current.data,end=" ->")           
   current=current.next
print("none")   