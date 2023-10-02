def merge_sort(list):
    # sorts a list in ascending order
    # there are three main steps in this function
    # divide, conquer, combine
    # conquer = recursively sort sub-lists which created in previous step

    # stopping condition
    if len(list) <= 1:
        return list

    left_half,right_half =split(list)
    # recursive functions
    left=merge_sort(left_half)
    right=merge_sort(right_half)

    return merge(left,right) # merge_sort final output

# defining the split function which used before

def split(list):
    # purpose = divide the main list into two sub-lists and returns those two lists
    mid=len(list)//2
    left=list[:mid]
    right=list[mid:]

    return left,right


# defining the merge function which used before

def merge(left,right):
    # used to merge two list which split before

    l=[]
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            l.append(left[i])
            i+=1

        else:
            l.append(right[j])
            j+=1
    """
    answer to the biggest problem ;
    question = after appending all the elements, why there are two while conditions after ?
    answer = imagine if the left list is one element shorter than the right list, when the left list 
    got 1 element, the while loops ends. due to the "and" condition it terminates the loop. so there can be
    one or more elements left in right list. 
    
    And that's why the following loops needed to write
    
    """

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

sample_list = [4,8,5,3,7,1,2,6,9]
sorted_list = merge_sort(sample_list)
print("sorted list :",sorted_list)


# now let's define a function to verify whether the list is sorted or not

def is_sorted(list):

    # stopping condition
    if len(list)==0 or len(list)==1 :
        return True
    # recursive (deep ; hard to understand)
    return list[0]<list[1] and is_sorted(list[1:])

print(is_sorted(sample_list))
print(is_sorted(sorted_list))










