anagram=["eat","ate","tan","tea","nat","bat"]
sort={}
for i in anagram :

    key = ''.join(sorted(i))
       
    if key not in sort :
        sort[key] = []
    sort[key].append(i)


print(sort)
new_array = list(sort.values())
print(new_array)


  
 
    