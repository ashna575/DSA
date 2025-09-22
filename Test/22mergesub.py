arr1=[3,6,9,0,0]
arry2=[4,10]


s = arr1+arry2
print(sorted(s))
n = len(arr1)
m = len(arry2)

# for i in range(n-1, -1, -1):
     
#  for j in range(m-1, -1, -1):
#         if i > j:
#             s.append(arr1[i])
#         else:
#             s.append(arr2[j])

# print(s)

def mergeArrays(arr1, arr2, m, n):
   
    arr1 = arr1[:m]
   
    arr1.extend(arr2)
    
    # Sort merged array
    arr1.sort()
    
    return arr1

