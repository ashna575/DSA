class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5


head=n1
slow=head
fast=head
current=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next   

print(slow.data)

    