# Laboratory Assignment #5 - Linked List

class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None
    
    def set_next(self, next):
        self.next = next
    
    def set_element(self, element):
        self.element = element
    
    def get_next(self):
        return self.next
    
    def get_element(self):
        return self.element

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def add(self, element):
        new_node = Node(element)
        curr = self.head
        while curr.next !=None:
            curr = curr.next
        curr.next = new_node
    
    def add_beginning(self, element):
        new_node = Node(element)
        new_node.set_next(self.head)
        self.head = new_node
    
    def add_after(self, element, position):
        element = Node(element)
        count = -1
        current = self.head
        if position == 1:
            element.next = self.head
            self.head = element
        while current:
            if count+1 == position:
                element.next = current.next
                current.next = element
                return
            else:
                count+=1
                current = current.next
        pass

    def delete(self, element):
        current = self.head
        previous = None
        while current !=None:
            if current.element == element:
                break
            previous = current
            current = current.get_next()
        if current == None:
            print(f"There is no element {element} found in the list")

        if previous == None:
            self.head = current.next
        else:
            if current !=None:
                previous.set_next(current.get_next())
            else:
                pass

    def count(self):
        curr = self.head
        total = 0
        while curr.next !=None:
            total += 1
            curr = curr.next
        return total
    
    def display(self, n):
        elements = []
        curr_node = self.head
        while curr_node.next !=None:
            curr_node = curr_node.next
            elements.append(curr_node.element)
        n = int(n)
        if n == 1:
            elements = elements
        if n == 2:
            elements.reverse()
        print("List is:", end=" ")
        for val in elements:
            print(val, "->", end=' ')
        print("")
    
    def search(self, element):
        item = self.head
        while item !=None:
            if item.get_element() == element:
                return item.element
            else:
                item = item.get_next()
    
    def search_pos(self, search):
        current = self.head
        pos = 0
        while current:
            if current.element == search:
                return pos
            current = current.next
            pos = pos + 1
        
    

def main():
    my_list = LinkedList()
    while True:    
        operation = int(input("Linked List: What do you want to do?\n1. Create a List\n"
        "2. Add an element at the beginning\n3. Add an element after a certain position\n"
        "4. Delete an element\n5. Display the list\n6. Count the elements in the list\n"
        "7. Reverse the list\n8. Search an element\n9. Quit\n\nEnter your choice here: "))

        if operation == 1:
            n = int(input("How many nodes you want?: "))
            for i in range(0,n):
                element = int(input("Enter the element: "))
                my_list.add(element)
            my_list.display(1)
            print("------------------------------------------------------")
        if operation == 2:
            begin_element = int(input("Enter the element you want to add: "))
            my_list.add_beginning(begin_element)
            my_list.delete(None)
            my_list.add_beginning(begin_element)
            my_list.display(1)
            print("------------------------------------------------------")
        if operation == 3:
            new_element = int(input("Enter the element you want to add: "))
            position = int(input("Enter the position you want your element to be added after: "))
            my_list.add_after(new_element, position)
            my_list.display(1)
            print("------------------------------------------------------")
        if operation == 4:
            delete_element = int(input("Enter the element you want to delete: "))
            my_list.delete(delete_element)
            print("The element has been deleted")
            print("------------------------------------------------------")
        if operation == 5:
            my_list.display(1)
            print("------------------------------------------------------")
        if operation == 6:
            count = my_list.count()
            print(f"The number of elements are: {count}")
            print("------------------------------------------------------")
        if operation == 7:
            my_list.display(2)
            print("------------------------------------------------------")
        if operation == 8:
            search_element = int(input("Enter the element you want to search: "))
            search = my_list.search(search_element)
            pos = my_list.search_pos(search)
            if search == None:
                print(f"There is no element {search_element} found in the list")
            else:
                print(f"Element {search} found at position {pos}")
            print("------------------------------------------------------")
        if operation == 9:
            print("------------------------------------------------------")
            break

main()