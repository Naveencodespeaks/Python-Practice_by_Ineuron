f = open("Range Rover.txt","r")
print("This is my code to handle an exception")
try:
    a = 10
    a/0
except Exception as e:
    print(e)
    print("This will be my final code after handling an exception")


try:
    f = open("naveen.txt","r")
except Exception as e:
    print(e)

try:
    f = open("sudh.txt", "r")
    f.write("This is my suspicuous code")
except Exception as e:
    print(e)
    print("This is not my suspicious set of the code")


# finally
print("#finally")

try:
    f = open("sudh.txt", "r")
    f.write("This is my suspicuous code")
except Exception as e:
    print(e)
    print("This is not my suspicious set of the code")
finally:
    print("This lock will be executes anytime")

print("@________In this we are using both try and exception____for both times___________@")

def askint():
    try:
        val = int(input("Please enter an integer"))
    except:
        print("No you have not entered an integer")
        try:
            val =int(input("please enter an integer"))
        except:
            print("We are able to handel your mistake second time")
    finally:
        print("Finally will be excecuted anytime")

askint()

print("#_____In this we are looping till we enter the integer_____#")

def askint1():
    while True:
        try:
            val = int(input("Please try to input an integer"))
            break
        except:
            print("looks like you have not entered an integer")
            continue
askint1()

