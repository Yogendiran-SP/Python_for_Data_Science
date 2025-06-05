def word_count(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=s.count(i)
    return d

def char_count(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=s.count(i)
    return d

print(word_count(input("Enter a list of strings: ").split()))
print(char_count(input("Enter a string: ")))