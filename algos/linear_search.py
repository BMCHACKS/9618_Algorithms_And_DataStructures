
def linear_search(to_find: str | int) -> int:
    '''
    takes the parameter `to_find` then searches
    for it till it locates the `index` of the value in an array \n 
    otherwise `returns -1` if value is not found 
    '''
    for x in range(len(array)):
        if to_find == array[x]: return x
    return -1

array = [0,1,2,3,4,99,100,999,-123,22]
print(linear_search(0)) # output will be 0
print(linear_search(22)) # output will be 9
print(linear_search(10000)) # output will be -1
print(linear_search(-123)) # output will be 8

