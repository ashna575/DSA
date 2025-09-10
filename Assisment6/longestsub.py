import heapq

def longest_unique_substring_heap(s):
    seen = {}
    start = 0
    heap = []

    for i, char in enumerate(s):
    
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i

     
      
