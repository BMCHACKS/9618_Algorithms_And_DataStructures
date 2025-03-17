# perfect stacks

# ////////////////////

# method 1
size = 10
stack = [-1]*size # <-- can be used :)

# method 2 
size = 10
stack = [-1 for _ in range(size)] # <-- recommended  << applies to when making objects as well >>  

# ////////////////////

# make global variable: `Head`
# NOTE `Head` can point both at the NEXT FREE SPACE or LAST VALUE ADDED
# It depends on the question

Head = 0 # in this case, head points towards the next free space 

def push(to_push: str | int) -> bool:
    '''
    takes a `to_push` and if the value is pushed returns `True` else `False` \n
    '''
    global Head, size
    # if head == size, meaning that head is more than the most index we can access
    if Head == size: return False
    stack[Head] = to_push
    Head += 1

    return True # return true to show that data was added


def pop() -> int | str:
    '''
    removes the last value pointed to by the `Head`, then removes it and 
    returns it to the user.
    '''

    global Head

    # first check if stack is empty or not

    return_data = 0 # or "" depending on the data stored in the stack
    if Head == 0: return retrun_data

    Head -= 1
    return_data = stack[Head]

    return return_data

