def duplicate(str):
    stack=[]
    for ch in str:
        if stack  and stack[-1] == ch:
            stack.pop
        else :
         stack.append  (ch)
    return ''.join(stack)     


str="geeksforgeek"
print(duplicate(str))