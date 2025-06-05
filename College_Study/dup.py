def dup(l):
    dup=[]
    for i in l:
        if l.count(i)>1 and i not in dup:
                dup.append(i)
    return dup

l=list(map(int,input("Enter the list elements: ").split()))
print(dup(l))