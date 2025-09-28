def assign_cookies(greed, cookies):
    greed.sort()
    cookies.sort()
    
    child = 0
    cookie = 0
    
    while child < len(greed) and cookie < len(cookies):
        if cookies[cookie] >= greed[child]:
            child += 1  # Cookie satisfies the child
        cookie += 1  # Move to next cookie
    
    return child

# Test case
greed = [1, 2, 3]
cookies = [1, 1]
print(assign_cookies(greed, cookies))  # Output: 1
