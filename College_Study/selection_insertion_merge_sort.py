def selection(l):
    if len(l)<=1:
        return l
    for i in range(len(l)):
        min_index = i
        for j in range(i+1,len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i],l[min_index] = l[min_index],l[i]
    return l

def insertion(l):
    if len(l)<=1:
        return l
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

def merge_sort(l):
    if len(l) <= 1:
        return l  # Base case: already sorted

    mid = len(l)//2 if len(l)%2==0 else (len(l)//2)+1
    left_half = merge_sort(l[:mid])
    right_half = merge_sort(l[mid:])

    print(f"left_half: {left_half}\nright_half: {right_half}")

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    k=1
    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        print(f"Iteration {k} (result): {result}")
        k+=1

    # Add remaining elements
    print(f"Result before left adding: {result}")

    result.extend(left[i:])
    
    print(f"Result before right adding: {result}")
    
    result.extend(right[j:])

    print(f"Result after adding: {result}")

    return result


l=list(map(int,input("Enter the list elements: ").split()))
# print("Using selection sort:",selection(l))
# print("Using insertion sort:",insertion(l))
print("Using merge sort:",merge_sort(l))