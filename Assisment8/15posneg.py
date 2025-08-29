def rearrange_pos_neg(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    
    result = []
    i = j = 0
    turn_pos = True
    
    while i < len(pos) and j < len(neg):
        if turn_pos:
            result.append(pos[i])
            i += 1
        else:
            result.append(neg[j])
            j += 1
        turn_pos = not turn_pos
    
    # Append remaining elements
    result.extend(pos[i:])
    result.extend(neg[j:])
    
    return result

# Example
arr = [1, -2, 3, -4, 5, -6, -7, 8]
print("Original:", arr)
print("Rearranged:", rearrange_pos_neg(arr))
