for row in range(7):
    for col in range(5):
        if (row==0) or (row==6 and ( col!=6 or col!=4 or col!=5))or (col==2 ) :
            print("*",end="")
        else:
            print(end=" ")    
    print()

    