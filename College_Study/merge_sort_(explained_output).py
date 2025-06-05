def merge_sort_trace(arr, depth=0):
    indent = "    " * depth  # Indentation for clarity in tracing

    if len(arr) <= 1:
        print(f"{indent}Base case reached with list: {arr}")
        return arr

    mid = len(arr) // 2
    print(f"{indent}Splitting list: {arr} -> left_half and right_half")

    left_half = merge_sort_trace(arr[:mid], depth + 1)
    right_half = merge_sort_trace(arr[mid:], depth + 1)

    print(f"{indent}Merging left_half: {left_half} and right_half: {right_half}")

    merged = merge_trace(left_half, right_half, depth + 1)

    print(f"{indent}Merged into: {merged}\n")
    return merged

def merge_trace(left, right, depth):
    indent = "    " * depth
    result = []
    i = j = 0
    iteration = 1

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        print(f"{indent}Iteration {iteration}: {result}")
        iteration += 1

    if i < len(left):
        print(f"{indent}Adding remaining from left: {left[i:]}")
    if j < len(right):
        print(f"{indent}Adding remaining from right: {right[j:]}")

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example run
lst = [6, 1, 4, 3, 5, 7, 9, 2, 8, 0]
print("Starting merge sort with tracing:\n")
sorted_list = merge_sort_trace(lst)
print("Final sorted list:", sorted_list)
