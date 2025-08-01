# rows=5
# for i in range(1,rows+1):
#    for space in range(rows):
#         print(' 1', end='')

#    for star in range(i):
#         print('*', end='')
         
rows = 5 

for i in range(rows, 0, -1):
    print(' '* (rows-i)+"*"*i)