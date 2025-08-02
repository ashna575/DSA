def insert(intervals, newInterval):
    result = []
    inserted = False

    for current in intervals:
       
        if current[1] < newInterval[0]:
            result.append(current)

      
        elif current[0] > newInterval[1]:
            if not inserted:
                result.append(newInterval)
                inserted = True
            result.append(current)

        else:
            newInterval[0] = min(current[0], newInterval[0])
            newInterval[1] = max(current[1], newInterval[1])

   
    if not inserted:
        result.append(newInterval)

    return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

print(insert(intervals, newInterval))  

