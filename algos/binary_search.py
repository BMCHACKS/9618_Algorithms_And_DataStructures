# perfect binary search

def binary_search(this_array: list, to_search: int | str) -> int:
    '''
    (arrays are basically lists) \n
    `this_array` is the list to search in \n
    `to_search` is the value to find \n
    returns `-1` if value not found \n
    Takes a list and returns the index position of the value in the list \n
    List must be already sorted in accending order
    '''
    low, top = 0, len(this_array)-1
    while top >= low:
        mid = (low + top) // 2
        if this_array[mid] == to_search: return mid
        low, top = mid + 1 if this_array[mid] < to_search else low, mid - 1 if this_array[mid] > to_search else top
    return -1  



# # test

# array = [1,2,3,4,5,6,7,999]
# print(binary_search(array, 999)) # returns 7 
# print(binary_search(array, 1)) # returns 0 
# print(binary_search(array, 100)) # returns -1 
