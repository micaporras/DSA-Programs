# Lab Assignment No. 4

# Function for swapping elements
def swap(list0, a, b):
    element = list0[a]
    list0[a] = list0[b]
    list0[b] = element

# Function for selection sorting
def selection():
    print("SELECTION SORTING:")
    list1 = []
    element_type = ""
    while True:
        n = int(input("How many elements are there in your list? "))
        type = int(input("Choose the type of elements: [1]INTEGERS [2]LETTERS (Upper-case only)\n"
        "Enter your choice here: "))
        mode = int(input("Choose a sorting mode: [1]ASCENDING [2]DESCENDING [3] ALPHABETICALLY\n"
        "Enter your choice here: "))
        if type == 1:
            element_type = "INTEGERS"
        if type == 2:
            element_type = "LETTERS"
        print(f"Enter your {n} {element_type} here (PRESS 'ENTER' KEY TO ADD EACH {element_type}): ")
        for i in range(0,n):
            if type == 1:
                element = int(input())
            if type == 2:
                element = input()
            list1.append(element)
        print(f"This is your list: {list1}")
        # For sorting integers in ascending order
        if type == 1 and mode == 1:
            for s in range(0, n - 1):
                value = list1[s]
                minimum = s
                for j in range(s, n):
                    if list1[j] < value:
                        value = list1[j]
                        minimum = j 
                swap(list1, s, minimum)
                print(f"PASS {s+1}: {list1}")
            print(F"FINAL SORTED ELEMENTS: {list1}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()
        # For sorting integers in descending order
        if type == 1 and mode == 2:
            for s in range(0, n - 1):
                value = list1[s]
                minimum = s
                for j in range(s, n):
                    if list1[j] > value:
                        value = list1[j]
                        minimum = j 
                swap(list1, s, minimum)
                print(f"PASS {s+1}: {list1}")
            print(F"FINAL SORTED ELEMENTS: {list1}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()
        # For sorting letters alphabetically 
        if type == 2 and mode == 3:
            for s in range(0, n - 1):
                value = list1[s]
                minimum = s
                for j in range(s, n):
                    if list1[j] < value:
                        value = list1[j]
                        minimum = j 
                swap(list1, s, minimum)
                print(f"PASS {s+1}: {list1}")
            print(F"FINAL SORTED ELEMENTS: {list1}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()

# Function for bubble sorting
def bubble():
    print("BUBBLE SORTING:")
    list2 = []
    element_type = ""
    while True:
        n = int(input("How many elements are there in your list? "))
        type = int(input("Choose the type of elements: [1]INTEGERS [2]LETTERS (Upper-case only)\n"
        "Enter your choice here: "))
        mode = int(input("Choose a sorting mode: [1]ASCENDING [2]DESCENDING [3] ALPHABETICALLY\n"
        "Enter your choice here: "))
        if type == 1:
            element_type = "INTEGERS"
        if type == 2:
            element_type = "LETTERS"
        print(f"Enter your {n} {element_type} here (PRESS 'ENTER' KEY TO ADD EACH {element_type}): ")
        for i in range(0,n):
            if type == 1:
                element = int(input())
            if type == 2:
                element = input()
            list2.append(element)
        print(f"This is your list: {list2}")
        # For sorting integers in ascending order
        if type == 1 and mode == 1:
            for b in range(0, n - 1):
                for j in range(0, n - 1 - b):
                    if list2[j] > list2[j + 1]:
                        swap(list2, j, j + 1)
                print(f"PASS {b+1}: {list2}")
            print(F"FINAL SORTED ELEMENTS: {list2}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()
        # For sorting integers in descending order
        if type == 1 and mode == 2:
            for b in range(0, n - 1):
                for j in range(0, n - 1 - b):
                    if list2[j] < list2[j + 1]:
                        swap(list2, j, j + 1)
                print(f"PASS {b+1}: {list2}")
            print(F"FINAL SORTED ELEMENTS: {list2}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()
        # For sorting letters alphabetically 
        if  type == 2 and mode == 3:
            for b in range(0, n - 1):
                for j in range(0, n - 1 - b):
                    if list2[j] > list2[j + 1]:
                        swap(list2, j, j + 1)
                print(f"PASS {b+1}: {list2}")
            print(F"FINAL SORTED ELEMENTS: {list2}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()

# Function for insertion sorting
def insertion():
    print("INSERTION SORTING:")
    list3 = []
    element_type = ""
    while True:
        n = int(input("How many elements are there in your list? "))
        type = int(input("Choose the type of elements: [1]INTEGERS [2]LETTERS (Upper-case only)\n"
        "Enter your choice here: "))
        mode = int(input("Choose a sorting mode: [1]ASCENDING [2]DESCENDING [3] ALPHABETICALLY\n"
        "Enter your choice here: "))
        if type == 1:
            element_type = "INTEGERS"
        if type == 2:
            element_type = "LETTERS"
        print(f"Enter your {n} {element_type} here (CLICK 'ENTER' TO ADD EACH {element_type}): ")
        for i in range(0,n):
            if type == 1:
                element = int(input())
            if type == 2:
                element = input()
            list3.append(element)
        print(f"This is your list: {list3}")
        # For sorting integers in ascending order
        if type == 1 and mode == 1:
            for i in range(1, n):
                value = list3[i]
                space = i
                while space > 0 and list3[space - 1] > value:
                    list3[space] = list3[space - 1]
                    space -= 1
                list3[space] = value
                print(f"PASS {i-1+1}: {list3}")
            print(F"FINAL SORTED ELEMENTS: {list3}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()
        # For sorting integers in descending order
        if type == 1 and mode == 2:
            for i in range(1, n):
                value = list3[i]
                space = i
                while space > 0 and list3[space - 1] < value:
                    list3[space] = list3[space - 1]
                    space -= 1
                list3[space] = value
                print(f"PASS {i-1+1}: {list3}")
            print(F"FINAL SORTED ELEMENTS: {list3}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()
        # For sorting letters alphabetically 
        if type == 2 and mode == 3:
            for i in range(1, n):
                value = list3[i]
                space = i
                while space > 0 and list3[space - 1] > value:
                    list3[space] = list3[space - 1]
                    space -= 1
                list3[space] = value
                print(f"PASS {i-1+1}: {list3}")
            print(F"FINAL SORTED ELEMENTS: {list3}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()

# Function for splitting a list in half and sorting it
def merge(list0, mode):
    if len(list0) > 2:
        middle = len(list0)//2
        sl1 = list0[:middle]
        sl2 = list0[middle:]
        print(sl1, sl2)
        merge(sl1, mode)
        merge(sl2, mode)
        # For sorting in ascending order or alphabetically
        if mode == 1 or mode == 3:
            sl1 = list(sl1)
            sl1.sort()
            print(sl1)
            sl2 = list(sl2)
            sl2.sort()
            print(sl2)
        # For sorting in descending order
        elif mode == 2:
            sl1 = list(sl1)
            sl1.sort(reverse=True)
            print(sl1)
            sl2 = list(sl2)
            sl2.sort(reverse=True)
            print(sl2)

# Function for merge sorting
def merge_sort():
    print("MERGESORTING:")
    list4 = []
    element_type = ""
    while True:
        n = int(input("How many elements are there in your list? "))
        type = int(input("Choose the type of elements: [1]INTEGERS [2]LETTERS (Upper-case only)\n"
        "Enter your choice here: "))
        mode = int(input("Choose a sorting mode: [1]ASCENDING [2]DESCENDING [3] ALPHABETICALLY\n"
        "Enter your choice here: "))
        if type == 1:
            element_type = "INTEGERS"
        if type == 2:
            element_type = "LETTERS"
        print(f"Enter your {n} {element_type} here (CLICK 'ENTER' TO ADD EACH {element_type}): ")
        for i in range(0,n):
            if type == 1:
                element = int(input())
            if type == 2:
                element = input()
            list4.append(element)
        print(f"This is your list: {list4}")
        # For sorting integers in ascending order
        if type == 1 and mode == 1:
            merge(list4, mode)
            list4.sort()
            print(f"FINAL SORTED ELEMENTS: {list4}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit() 
        # For sorting integers in descending order
        if type == 1 and mode == 2:
            merge(list4, mode)
            list4.sort(reverse=True)
            print(f"FINAL SORTED ELEMENTS: {list4}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()
        # For sorting letters alphabetically 
        if type == 2 and mode == 3:
            merge(list4, mode)
            list4.sort()
            print(f"FINAL SORTED ELEMENTS: {list4}")
            again = input("Do you want to try again?[y/n]: ")
            if again == "y":
                Main()
            if again == "n":
                print("**********************END************************")
                exit()

# Function for Main Program
def Main():
    print("********* SORTING ALGORITHM APPLICATION *********\n*      "
    "Programmed by: Porras, Mica Lorraine     *\n*                   "
    "BSCOE 2-1                   *")

    while True:
        select = int(input("*             < < < MAIN MENU > > >             *\n*"
        "            (1) SELECTION SORTING              *\n*"
        "            (2) BUBBLE SORTING                 *\n*"
        "            (3) INSERTION SORTING              *\n*"
        "            (4) MERGE SORTING                  *\n*"
        "            (5) EXIT                           *\n"
        "Select an option: "))
        if select == 1:
            selection()
        if select == 2:
            bubble()
        if select == 3:
            insertion()
        if select == 4:
            merge_sort()
        if select == 5:
            print("**********************END************************")
            break

Main()
