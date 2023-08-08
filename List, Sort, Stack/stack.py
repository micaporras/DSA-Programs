# Lab Assignment #6 - Stack

class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def __str__(self):
        current = self.head.next
        out = ""
        while current:
            out += str(current.element) + " "
            current = current.next
        return out[:-1]

    def Size(self):
        return self.size
    
    def push(self, element):
        node = Node(element)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def pop(self):
        delete = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return delete.element
    
def Main():
    stack = Stack()
    while True:
        menu = int(input(
        "********************************************\n"
        "************ My Stack Menu      ************\n"
        "************ 1. Push            ************\n"
        "************ 2. Pop             ************\n"
        "************ 3. Display Stack   ************\n"
        "************ 4. Exit            ************\n"
        "********************************************\n"
        "Enter your choice: "))

        if menu == 1:
            element = int(input("Enter the number to be pushed into the stack: "))
            stack.push(element)
        if menu == 2:
            size = stack.Size()
            if size == 0:
                print("The stack is empty - Stack Underflow!")
            else:
                element = stack.pop()
                print(f"The popped element is: {element}")
        if menu == 3:
            size = stack.Size()
            if size == 0:
                print("Contents of the stack is:\nStack Underflow!")
            else:
                print(f"Contents of the stack is:\n{stack}")
        if menu == 4:
            break

Main()