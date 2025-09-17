def reverse_words(s):
    words = s.strip().split()
    words.reverse()
    
    return " ".join(words)


s = "the sky is blue"
print(reverse_words(s))  
