#reverse word in a string 
#input the sky is blue
#out:blue is sky the
def reverse_string(a):
    stack = []
    for ch in a:
        stack.append(ch)

    rev = ""
    while stack:
        rev += stack.pop()
    return rev
s="the sky is blue"
a=[]

    
print(s)
print(reverse_string(s))
    
