

'''
There are 2 types of binary trees in questions

1. Made with OOP
2. Made with 2D-Array


Now binary trees hae these things

-> Make the binary tree

-> Add Data
-> Search For Data

-> Output InOrder USING RECURSION ONLY 
-> Output PostOrder USING RECURSION ONLY 

'''

# ADD DATA is ALWAYS IN ORDER for a BINARY TREE
def Add(data):
    global root, NextFree
    # we firstly check if there is SPACE or not
    if NextFree == -1:
        print("[ERROR] BinaryTree is full!")
    else:
        # meaning there is atleast 1 space
        New = NextFree
        BinaryTree[New].data = data
        NextFree = BinaryTree[New].leftpointer
        BinaryTree[New].leftpointer = -1
        if root == -1:
            # meaning its the VERY FIRST node to be added
            root = New
        else:
            # meaning there are more nodes
            # we have to find the LOCAION for the new data
            # we'll start from the FIRST / ROOT node
            current = root
            # now we'll need a variable named `smaller` which'll indiacte
            # if the root is to be placed on the left or right
            smaller = False
            while current != -1:
                previous = current
                if data > BinaryTree[current].data:
                    current = BinaryTree[current].rightpointer
                    smaller = False
                else:
                    current = BinaryTree[current].leftpointer
                    smaller = True

            # now we'll place the node
            if smaller:
                BinaryTree[previous].leftpointer = New
            else:
                BinaryTree[previous].rightpointer = New

def InOrder(root):
    if BinaryTree[root].leftpointer != -1: InOrder(BinaryTree[root].leftpointer)
    print(BinaryTree[root].data, end=" ")
    if BinaryTree[root].rightpointer != -1: InOrder(BinaryTree[root].rightpointer)


def PostOrder(root):
    if BinaryTree[root].leftpointer != -1: PostOrder(BinaryTree[root].leftpointer)
    if BinaryTree[root].rightpointer != -1: PostOrder(BinaryTree[root].rightpointer)
    print(BinaryTree[root].data, end=" ")


# IGNORE this output function below; it's for testing purposes only! 
def Output_BinaryTree():
    for x in range(len(BinaryTree)):
        print(f"index: {x} | leftpointer: {BinaryTree[x].leftpointer} | data: {BinaryTree[x].data} | rightpointer: {BinaryTree[x].rightpointer}")
    print(f"root: {root} | nextFree: {NextFree}")


# main

class Node:
    def __init__(self):
        self.leftpointer = -1
        self.data = ""
        self.rightpointer = -1

size = 5
BinaryTree = [Node() for _ in range(size)]
root = -1
NextFree = 0

# so far its like a linkedlist
# now let's make the leftpointer point to the NEXT index so the bt can be connected

for x in range(len(BinaryTree)):
    BinaryTree[x].leftpointer = x+1

# finally make the LAST pointer NULL

BinaryTree[4].leftpointer = -1


# IGNORE CODE BELOW, ITS FOR TESTING PURPOSES ONLY
while True:
    print()
    choice = int(input("Enter 1 to Add, 2 for Inorder, 3 for postorder > "))
    match choice:
        case 1 : Add(input("Enter data > "))
        case 2 : 
            InOrder(root) 
            print()
        case 3 : 
            PostOrder(root)
            print()
    Output_BinaryTree()
    print()
