def mean(l):
    return sum(l)/len(l)

def median(l):
    if len(l)%2==0:
        return ((l[len(l)//2])+(l[(len(l)//2)-1]))/2
    else:
        return l[len(l)//2]

def mode(l):
    max_count=0
    for i in l:
        if l.count(i)>max_count:
            max_count=l.count(i)
    mode=[]
    for i in set(l):
        if l.count(i) == max_count:
            mode.append(i)
    return mode

print("Enter the elements of the list:")
l=list(map(int,input().split()))
print("Mean of the list: ",round(mean(l),1))
print("Median of the list: ",median(l))
print("Mode of the list: ",mode(l))