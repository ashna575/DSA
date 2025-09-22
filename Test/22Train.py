arrival=[900,940,950]
departure=[910,1200,1120]
count=1

for i in range(1,len(arrival)):
    for j in range(0,len(departure)):
        if arrival[i] < departure[j]:
            count +=1
        
print(count)    
                