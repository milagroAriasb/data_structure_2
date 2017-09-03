#Sorting

#I use the demo as a reference for  this assigment. 

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    
    for i in range(len(lst) - 1):
        swap = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
                if i == (len(lst) - 2):
                    return lst
        if not swap:
            break


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    results = []
    while len(list1) > 0 or len(list2) > 0:
        if list1 == []: #if this list is empty
            results.append(list2.pop(0)) #appen list2 to the restults
        elif list2 == []: #if this list is empty 
            results.append(list1.pop(0)) #append list1 to restuls
        elif list1[0] < list2[0]:# if item in list1 in position 0 is less than item in list2 in same position
            results.append(list1.pop(0)) #append item in list1 to results
        else: # if item in list1 in position 0 is greater than item in list2 in same position
            results.append(list2.pop(0))#append item in list2 to results

    return results



##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    pass
    # we have to create 2 lists by cutting the current list in half and we 
    # call merge_lists (f_hald_list, s_half_list) 




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
