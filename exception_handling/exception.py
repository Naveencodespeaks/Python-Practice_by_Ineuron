
a = int(input("enter first number"))
b = int(input("enter second number"))
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("b should not be a zero")
print("-----------------------------------------------------------------------")

a = int(input("enter first number"))
b = int(input("enter second number"))
try:
    c = a / b
    print(c)
except :
    print("b should not be a zero")
d = a+b
print(d)

print("------------------------------------------------------------------------------------")


a = int(input("enter first  number"))
b = int(input("Enter second number"))
try:
    c = a/b
    print(c)
except:
    print("Please enter only non zero integer")
print("--------------------------------------------------------------------------------------------------")



a = int(input("Enter a first number"))
b = int(input("Enter a second number"))

try:
    c = a/b
    print(c)
    d = int(a)+b
    print(d)
except ZeroDivisionError:
    print("B should not be a zero")
except ValueError:
    print("Please input number only")

print("=====================================================================")

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a/b
        print(c)
        break
    except ZeroDivisionError:
        print("Non Zero denominator")
    except ValueError:
        print("There should not be string")

while True:
    try:
        a = int(input("First number"))
        b = int(input("second number"))
        c = a/b
        print("div :", c)
        break
    except ZeroDivisionError as e:
        print(e)



print("----*******************____________________**********************------------------------------")



import sys
while True:
    try:
        a = int(input("Enter a first number"))
        b = int(input("Enter a second number"))
        c = a/b
        print("div:",c)
        break
    except:
        print(sys.exc_info())


# EXCEPTION HANDLING BY SUDHANSHU SIR!!!!!!!


a = int(input("enter first number"))
b = int(input("enter second number"))
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("b should not be a zero")
print("----------------------------------------------------------_________-------------")

a = int(input("enter first number"))
b = int(input("enter second number"))
try:
    c = a / b
    print(c)
except :
    print("b should not be a zero")
d = a+b
print(d)

print("------------------------------------------------------------------------------------")


a = int(input("enter first  number"))
b = int(input("Enter second number"))
try:
    c = a/b
    print(c)
except:
    print("Please enter only non zero integer")
print("--------------------------------------------------------------------------------------------------")



a = int(input("Enter a first number"))
b = int(input("Enter a second number"))

try:
    c = a/b
    print(c)
    d = int(a)+b
    print(d)
except ZeroDivisionError:
    print("B should not be a zero")
except ValueError:
    print("Please input number only")

print("=====================================================================")

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = a/b
        print(c)
        break
    except ZeroDivisionError:
        print("Non Zero denominator")
    except ValueError:
        print("There should not be string")

while True:
    try:
        a = int(input("First number"))
        b = int(input("second number"))
        c = a/b
        print("div :", c)
        break
    except ZeroDivisionError as e:
        print(e)



print("----*******************____________________**********************------------------------------")



import sys
while True:
    try:
        a = int(input("Enter a first number"))
        b = int(input("Enter a second number"))
        c = a/b
        print("div:",c)
        break
    except:
        print(sys.exc_info())


# EXCEPTION HANDLING BY SUDHANSHU SIR!!!!!!!


print("# EXCEPTION HANDLING BY SUDHANSHU SIR!!!!!!!----------REVISION----------------------------")