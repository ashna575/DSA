class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
           return False 
        self.stack.pop()      
        
    def isEmpty(self):
       return len(self.stack)==0
            
mystack=stack()
mystack.push(2)
mystack.push(3)            


print(mystack.stack)
print(mystack.pop())
print("stack after pop:",mystack.stack)