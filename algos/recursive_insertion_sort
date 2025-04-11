def recursive_insertion_sort(array: list[int | str], i, j: int, key: int | str) -> list:
    if j >= 0 and key < array[j]:
        array[j+1] = array[j]
        return recursive_insertion_sort(array, i, j-1, key)

    array[j+1] = key
    if i+1 == len(array): return array
    return recursive_insertion_sort(array, i+1, i, array[i+1])

'''

This recursive insertion sort only works for arrays/list
which have at least 2 elements

for example:

some_unsorted_data = [1, 2, 3, -1, -2, -3, 0]
i = 1
j = i - 1
key = some_data[i]

some_data = recursive_insertion_sort(some_unsorted_data, i, j, key)

'''
