# Problem: Given a string s, return the longest palindromic substring in s.
 

# Example:
# Input: "babad" → Output: "bab" or "aba"


def longestPalindrome(s):
    start = 0
    max_len = 0

    for i in range(len(s)):
     
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

    return s[start:start + max_len]


s = "babad"
print(longestPalindrome(s))  
