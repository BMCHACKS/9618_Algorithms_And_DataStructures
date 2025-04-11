# perfect bubble sort

def bubble_sort(this_array: list) -> list:
    '''
    (arrays are lists) \n
    takes `this_array` and sorts it in accending order \n
    to sort it in decending order change condition `if this_array[y] > this_array[y+1]:` to `if this_array[y] < this_array[y+1]:`
    '''
    for x in range(len(this_array)):
        swap = False
        for y in range(len(this_array)-x-1):
            if this_array[y] > this_array[y+1]: 
                this_array[y], this_array[y+1]= this_array[y+1], this_array[y]
                swap = True
        if not swap: break
    return this_array


# # test
# array = [9,2,1,100,99,22]
# this_array = bubble_sort(array)
# print(this_array) # prints 1, 2, 9, 22, 99, 100
