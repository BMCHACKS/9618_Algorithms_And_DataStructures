# perfect insertion sort

def insertion_srot(this_array: list) -> list:
    '''
    (arrays are basically lists) \n
    takes `this_array` and sorts it \n
    change condition `while j >= 0 and key < this_array[j]:` to `while j >= 0 and key > this_array[j]:` to 
    sort it in decending order
    '''
    for i in range(1, len(this_array)):
        key = this_array[i]
        j = i - 1
        while j >= 0 and key < this_array[j]:
            this_array[j+1] = this_array[j]
            j -= 1
        this_array[j+1] = key
    return this_array


array = [999, -1, 0, 123, 1, 2, 3]
array = insertion_srot(array)
print(array) # prints -1 0 1 2 3 123 999




