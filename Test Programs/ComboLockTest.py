# Test Program for Lab Assignment 3.4 - THE COMBINATION LOCK

from ComboLock import ComboLock

def main():
    lock = ComboLock()
    dial = [15, 2, 26]

    while True:
        num1, num2, num3 = lock.ComboLock()
        user = input("The Combination Lock:\nWhat do you want to do?\nA.Display Dial\nB.Reset Dial\nC.Turn the Dial to the left"
        "\nD.Turn the Dial to the right\nE.Open the Lock\nF.Exit\n\nEnter your choice here: ")
        if user == "A":
            print(f"The current combination in the dial is: {dial[0]}, {dial[1]}, {dial[2]}")
            print("-----------------------------------------------------------------------------------------------------")
        if user == "B":
            dial[0] = lock.reset()
            dial[1] = lock.reset()
            dial[2] = lock.reset()
            print("-----------------------------------------------------------------------------------------------------")
        if user == "C":
            combNum = int(input("What do you want to turn? The first, second, or third dial in the combination lock?(1/2/3):"))
            if combNum == 1:
                turn = lock.turnLeft(1)
                dial[0] = dial[0] + turn
            if combNum == 2:
                turn = lock.turnLeft(1)
                dial[1] = dial[1] + turn
            if combNum == 3:
                turn = lock.turnLeft(1)
                dial[2] = dial[2] + turn
            print("-----------------------------------------------------------------------------------------------------")
        if user == "D":
            combNum = int(input("What do you want to turn? The first, second, or third dial in the combination lock?(1/2/3):"))
            if combNum == 1:
                turn = lock.turnRight(1)
                dial[0] = dial[0] + turn
            if combNum == 2:
                turn = lock.turnRight(1)
                dial[1] = dial[1] + turn
            if combNum == 3:
                turn = lock.turnRight(1)
                dial[2] = dial[2] + turn
            print("-----------------------------------------------------------------------------------------------------")
        if user == "E":
            if dial[0] == num1 and dial[1] == num2 and dial[2] == num3:
                lock.open()
                break
            else:
                print("Wrong combination. Try Again") 
                print("-----------------------------------------------------------------------------------------------------")
        if user == "F":
            break
    

main()
