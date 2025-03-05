
# linkedlists can be either ordered or un-ordered
# this one is for ordered
def Add(data: str):
    global start, free

    # check if linkedlist if free or not
    if free == -1:
        print("[ERROR] LinkedList is full!")
    # else we add the node
    else:
        # first see if its the FIRST node we're adding
        new = free
        LinkedList[new].data = data
        free = LinkedList[new].pointer
        LinkedList[new].pointer = -1

        if start == -1:
            start = new
        else:
            # now we'll find a location for the node
            current = start
            while current != -1 and data > LinkedList[current].data:
                previous = current
                current = LinkedList[current].pointer
            # meaning we need to place this new node is now the new START node
            if current == start:
                LinkedList[new].pointer = start
                start = new
            else:
                # meaning we're adding a node BETWEEN 2 nodes or else that node 
                # is the LAST node
                LinkedList[new].pointer = LinkedList[previous].pointer
                LinkedList[previous].pointer = new


# there are 2 types of remove procedures in LinkedList questions
# one which make you just remove the last / first value

# second which make you SEARCH for a specific value then remove it

# for this code, we'll be doing the second one
def Remove(to_remove):
    global start, free


    # now we need to remove data
    # first - check if linkedlist is empty or not
    if start == -1: 
        print("[ERROR] LinkedList is empty!")
    else:
        # if start != -1 - We have SOMETHING to remove

        # second step - Find what we need to remove
        current = start
        while current != -1 and LinkedList[current].data != to_remove:
            previous = current
            current = LinkedList[current].pointer
        
        # after this loops end, either we'll have found the value or not

        # third step - Check if we found it or not

        if current == -1:
            print("[ERROR] Value not found!")
        else:
            # meaning we've found the value 
            # step 4 - now remove the value and adjust the pointers

            # we dont have to do this, but for this case we'll overwrite the data in that pos with "removed" 
            LinkedList[current].data = "removed"
            nextNode = LinkedList[current].pointer
            if current == start:
                start = nextNode
            else:
                # meaning ITS not the first value, it maybe the second, third or last
                LinkedList[previous].pointer = nextNode
            
            # we also gotta now fix the pointer for FREE 
            LinkedList[current].pointer = free
            free = current
    
        
def Output_LinkedList():
    current = start
    while current != -1:
        print(LinkedList[current].data)
        current = LinkedList[current].pointer


# THIS OUTPUT IS MADE FOR TESTING CODE ONLY!
def Output():
    global start, free
    for x in range(len(LinkedList)): 
        print(f"index: {x} | data: {LinkedList[x].data} | pointer: {LinkedList[x].pointer}")
    print(f"start: {start} | free: {free}")


# main

class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

size = 5
LinkedList = [Node("", x+1) for x in range(size)]
LinkedList[4].pointer = -1
start = -1
free = 0


# IGNORE CODE BELOW, ITS FOR TESTING PURPOSES ONLY
Output()

while True:
    choice = int(input("1 to add | 2 to remove > "))
    Add(input("What to add > ")) if choice == 1 else Remove(input("What to remove > ")) 
    choice = input("Output data in order? [enter y] > ")
    if choice == "y": Output_LinkedList()
    Output()


