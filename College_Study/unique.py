def col_unique(l):
    uni=[]
    for i in l:
        if i not in uni:
            uni.append(i)
    return uni

def unique(l):
    uni=[]
    for i in l:
        if l.count(i)==1 and i not in uni:
            uni.append(i)
    return uni

l=list(map(int,input("Enter the list elements: ").split()))
print("College Unique:\n",col_unique(l))
print("My Unique:\n",unique(l))