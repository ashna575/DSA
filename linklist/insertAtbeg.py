class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
n1=Node(10)
n2=Node(20)
n3=Node(43)
n4=Node(24)

n1.next=n2
n2.next=n3
n3.next=n4

head=n1
new_ele=Node(68)
new_ele.next=head
head=new_ele

current=head
while current is not None:
    print(current.data,end=" -> ")
    current=current.next
    
