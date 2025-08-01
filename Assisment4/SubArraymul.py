def maxmulti(arry):
    maxmium=arry[0]
    current=arry[0]
    
    for i in range(1,len(arry)):
        currentNo= max(arry[i],current*arry[i])
        maxmium=max(currentNo,maxmium)
        return maxmium


arry=[2,3,-2,4]
print(maxmulti(arry))