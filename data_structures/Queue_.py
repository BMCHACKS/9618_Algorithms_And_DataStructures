
'''
There are 2 types of queue in the exam

1. Linear Queue
2. Circular Queue

^ both are fairly simple and the only difference is how their functions (Enqueue & Dequeue) operate

NOTE: Sometimes the Queue is made with OOP or just like below with an Array and pointers
'''

def Enqueue(data):
    global HeadPointer, TailPointer, Free

    # let's check if Queue if full or not
    if Free == 0:
        # meaning there are ZERO spaces left
        print("[ERROR] Queue is full!")
    else:
        # meaning there is some spaces left
        Queue[TailPointer] = data
        TailPointer += 1
        Free -= 1
        
        if HeadPointer == -1: HeadPointer = 0
        
        '''
        
        check if tailpointer is greater than
        available index positions.
        
        In this case we have 0-4 index
        so total size = 5

        if TailPointer equal size we have to 
        WRAP it around. 
        This is what makes a `circular` queue

        '''
        if TailPointer == size: TailPointer = 0


def Dequeue():
    global HeadPointer, TailPointer, Free

    # let's check if Queue is empty or not
    if Free == 5:
        print("[ERROR] Queue is empty!")
    else:
        return_data = Queue[HeadPointer]
        HeadPointer += 1
        # since we've removed data, there is 1 more Free space
        Free += 1
        # same reason as TailPointer in Enqueue()
        if HeadPointer == size: HeadPointer = 0

        # here we reset HeadPointer & TailPointer since, there are NO MORE ELEMENTS LEFT
        if Free == 5: HeadPointer, TailPointer = -1, 0

        print(f"Data removed > {return_data}")
    

# main

# lets make a circular Queue

size = 5
Queue = ["" for _ in range(size)]


# we now need to make the Head, Tail and Free pointers 
# HeadPointer in this case points to the FIRST element in the Queue
# TailPointer in this case points to the NEXT free space in the Queue 
HeadPointer = -1
TailPointer = 0
Free = size

# IGNORE CODE BELOW, ITS FOR TESTING PURPOSES ONLY
while True:
    choice = int(input("Enter 1 for Enqueue, 2 for Dequeue > "))
    match choice:
        case 1 : Enqueue(input("Enter data > "))
        case 2 : Dequeue()


