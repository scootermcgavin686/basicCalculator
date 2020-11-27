import Calculations as C

Quit = False
newNum = True
num1 = 0
num2 = 0
instructions = "Please press:\n 1: for addition \n 2: for subtraction \n 3: for multiplication \n 4: for division \n 5: for Modulo \n N: for new numbers \n Q: to quit"

def calculation(userCalc):
    global Quit
    global newNum
    if userCalc == "1":
        print("Your number now is", end=" ")
        print(C.addition(num1,num2))
    elif userCalc == "2":
        print("Your number now is", end=" ")
        print(C.subtraction(num1,num2))
    elif userCalc == "3":
        print("Your number now is", end=" ")
        print(C.multiplication(num1, num2))
    elif userCalc == "4":
        print("Your number now is", end=" ")
        print(C.division(num1, num2))
    elif userCalc == "5":
        print("Modulo num1 is: ", end=" ")
        print(C.modulo(num1,num2))
    elif userCalc == "Q":
        print("You have ended the program")
        Quit = True
    elif userCalc == "N":
        newNum = True
    else:
        print("Not a valid selection, please try again.")

    return

print(instructions)

while Quit == False:
    while newNum == True:
        try:
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            newNum = False
        except:
            print("An Error has occurred, try again.")

    userCalc = input("What calculation would you like to preform: ")
    calculation(userCalc)

print("Thank you for using Calculator")



