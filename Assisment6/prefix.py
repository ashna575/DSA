words = ["flower", "flow", "flight"]

prefix = words[0]


for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]  
        if prefix == "": 
            break;

print("Common prefix:", prefix)
