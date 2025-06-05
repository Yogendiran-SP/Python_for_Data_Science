def linear(l,a):
    for i in range(0,len(l)):
        if a==l[i]:
            return i+1
    else:
        return -1
    
def binary(l,a):
    l.sort()
    print("Sorted list:",l)
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == a:
            return mid
        elif l[mid] > a:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return -1

l=list(map(int,input("Enter the list elements: ").split()))
a=int(input("Enter the target element: "))

li=linear(l,a)
print(f"Element is found at position: {li}" if li!=-1 else "Element not found!")

b=binary(l,a)
print(f"Element found at index: {b}" if b!=-1 else "Element not found!")