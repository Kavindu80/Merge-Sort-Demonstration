# Merge Sort Algorithm

Merge Sort is a popular and efficient sorting algorithm that follows the divide-and-conquer approach to sort an array or list. It divides the input into smaller halves, sorts them separately, and then merges them back together in sorted order.

## How Merge Sort Works

1. **Divide**: Split the unsorted list into smaller sublists, each containing a single element (base case).

2. **Conquer**: Recursively merge and sort adjacent sublists to create larger sorted sublists until there is only one sorted sublist remaining.

3. **Merge**: Repeatedly merge two sorted sublists into a single, larger sorted sublist until the entire list is sorted.

## Pseudocode

Here's a basic pseudocode representation of the Merge Sort algorithm:

```python
function merge_sort(arr)
    if length(arr) <= 1
        return arr
    
    mid = length(arr) / 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)
    
function merge(left, right)
    result = []
    
    while left and right
        if left[0] <= right[0]
            result.append(left[0])
            left = left[1:]
        else
            result.append(right[0])
            right = right[1:]
    
    if left
        result.extend(left)
    if right
        result.extend(right)
    
    return result
