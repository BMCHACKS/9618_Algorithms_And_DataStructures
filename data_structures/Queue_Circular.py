
def Enqueue(value):
    global Head, Tail, Free, Size
    
    if Free == 0:
        print("There is no more space in the Q!")
    else:
        CircularQueue[Tail] = value
        Tail += 1
        Free -= 1
        
        if Head == -1:
            Head = 0
        if Tail > Size-1:
            Tail = 0

def Dequeue():
    global Head, Tail, Free, Size
    
    if Free == 7:
        print("Queue is empty! - Nothing to remove!")
        return ""
    else:
        Free += 1
        value = CircularQueue[Head]
        CircularQueue[Head] = ""
        Head += 1
        
        if Head > Size-1:
            Head = 0
        if Free == 7:
            Head = -1
            Tail = 0
        return value

Size          = 7
CircularQueue = ["" for _ in range(Size)]
Head          = -1 # Points towards the FIRST item in the q
Tail          = 0  # Points towards the NEXT FREE SPACE in a q
Free          = len(CircularQueue) # current amount of free spaces in the q

# --- below code for testing the code only ---
for x in range(20):
    choice = input("Enter 1 to enqueue, 2 to dequeue: ")
    if choice == "1":
        value = input("Enter a name to enqueue: ")
        Enqueue(value)
    elif choice == "2":
        value = Dequeue()
        if value != "":
            print(f"Dequeued : {value}")
    print(CircularQueue)


