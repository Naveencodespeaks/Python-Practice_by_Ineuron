def test():
    print("this is my first function")
test()
print(type(test()))

def test1():
    return "this is my first fun"
print(test1() + "sudh")

def test2():
    pass

def test3():
    return 1,2,3,[1,2,3,4,53,2,2]
print(test3())
print("----------------------------------------------")
def test4():
    a =10+5
    b =10+5
    return a,b
print(test4())

g = test4()

print(g)

k,l = test4()
print(k,l)
print(k)
print(l)

print("------------------------------------------------")
a= 10
b = 30
while a<b:
    print(a)
    a =a+1
else :
    print("print this is else object")

print("-------------------------------------------------")

def test5():
    a = 1
    b = 10
    while a<b:
        print(a)
        a= a+1
    else:
        print("print this is a else object")
print(test5())

print("****************************************************")

def test6(a,b):
    while a<=b:
        return a  # when we use return over here it only return one value
        a = a+1
    else:
        return("print this else object")
print(test6(7,20))

print("********************************************************")
def test6(a,b):
    l=[]
    while a<=b:
        l.append(a) # when we use list.append it return the total value's
        a = a+1
    else:
        print("print this else object")
        return l  # return should me inside the function other wise it through you an error
print("_________________________________________________________")

print(test6(3,18))

print("-------------------------------------------------------------")

v = [1,2,3,4,5,6,789,9,9,75,34,124,[1,9,8,6,54,3,21,4],"sudh"] # by using debugging you can understand the concept in deep way
def test7():
    z = []
    for i in v:
        if type(i) == int:
            z.append(i) # which append the values in to the z=[]
    return z # return the z value
print(test7())


print("--------------------------------------------------------------------------------------")
r = [1,2,3,4,5,67,8,9,2,[12,3,4,5,634,34124,3], "hare", "krishna","rama","harekrishna","harerama"]

def krish():
    p = []
    for i in r:
        if type(i) == str:
            p.append(i)
    return p
print(krish())

print("----------------------------------------------------")


R = ["hare", "krishna","hare","rama", "hare krishna hare krishna krishna krishna hare hare hare rama hare rama rama rama hare hare"]
def ramMandhir():
    K = []  # here K is in CAPITAL
    for i in R:
        if type(i) == str:
            K.append(i) # here K is in CAPITAL
    return K # here K is in CAPITAL
print(ramMandhir())













