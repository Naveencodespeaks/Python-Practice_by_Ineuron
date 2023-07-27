# define the functions needed, add, sub, mul, div
# print options to the user
# Ask for the values
# call the functions
# while  loop to continue the program until the user wants to exit


def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b)+ "=" + str(answer) + "\n")

def sub(a,b):
    answer = a-b
    print(str(a) + "-" + str(b)+ "=" + str(answer) + "\n")

def mul(a,b):
    answer = a*b
    print(str(a) + "*" +  str(b) + "=" + str(answer) + "\n")

def div(a,b):
    answer = a/b
    print(str(a)  + "/" +  str(b) + "=" + str(answer) + "\n")

def mol(a,b):
    answer = a%b
    print(str(a) + "%" + str(b) + "=" + str(answer) + "\n")

def sqr(a,b):
    answer = a**b
    print(str(a) +  "sqr"  + str(b) + "=" + str(answer) + "\n")

while True:
    print("A.Addition")
    print("B.Substraction")
    print("C.Multiplication")
    print("D.Division")
    print("E.percentail")
    print("F.square")
    print("G.Exit")


    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        add(a,b)
    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multipication")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        div(a,b)

    elif choice == "e" or choice == "E":
        print("square")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        sqr(a,b)

    elif choice == "f" or choice == "F":
        print("percentage")
        a = int(input("Input First number: "))
        b = int(input("input second number: "))
        mol(a,b)

    elif choice == "g" or choice == "G":
        print("program ended")
        quit()


