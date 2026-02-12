
def Enqueue(value):
    global Head, Tail, Size
    
    if Tail == Size:
        print("There is no more space in the Q!")
    else:
        LinearQueue[Tail] = value
        Tail += 1
        if Head == -1:
            Head = 0

def Dequeue():
    global Head, Tail
    
    if Head == -1:
        print("Queue is empty! - Nothing to remove!")
        return ""
    else:
        value = LinearQueue[Head]
        LinearQueue[Head] = ""
        Head += 1
        
        if Head == Tail:
            Head = -1
            Tail = 0
            
        return value

Size        = 7
LinearQueue = ["" for _ in range(size)]
Head        = -1 # Points towards the FIRST item in the q
Tail        = 0  # Points towards the NEXT FREE SPACE in a q


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
    print(LinearQueue)


