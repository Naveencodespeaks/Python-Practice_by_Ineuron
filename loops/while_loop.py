# while is a basic of loop

a = 1
b = 10

while a <=b:
    print(a)
    a = a+1

# while loop is a loop basicaly unless or untill it not going  to find out it not going to end  or until it gets a false condition it not gonna stop!!!

print("-------------------------------------------------------------")


a = 1
b = 10
while a<=b:
    print(a)
    a = a+2
else:
    print("print this is else block")


a = 1
b =10
while a<10:
    print(a)
    if a == 5:
        break
    a = a+1
else:
    print("print this ")

print("-------------------------------------------------")


a = 1
b = 10
while a < 10:
    print(a)
    if a ==7:
        break
    a = a+1
else:
    print("print this")

print("------------------------------------------------------------")

a = 10
b = 1333

while a <= b:
    print(a)
    if a == 123:
        break
    a = a+1
else :
    print("print This")

print("---------------------------------------------")


"""a = 1
b = 10
while a < b:
    print(a)
    if a ==3:
        continue     # this will be continue to infinite loop because we have using continue keyword
    a = a+1"""
print("----------------------------------------------------------------------------------------------------")

a = 1
b = 10
while a < b:
    a = a + 1
    if a ==3:
        continue   # here continue key word is use to give control to the while loop, to continue the loop so that we are not able to  see 3 in the output
    print(a)



l = [1,2,3,53,2,4,523,5435,35,6,3,21]

for i in l:
    print(i)
print("----------------------------------------------------------------------------------------------")

a = 0
while a < len(l):
    print(l[a])
    a = a + 1

print("----------------------------------------------------")

a = 0

while a < len(l):
    print(l[a])
    a = a+1
print("---------------------------------------------------------------")



t = (3,4,5,6,7,8,9)

a = 0
while a< len(t):
    if t[a] == 6 or t[a] == 7:
        print(a)
    a = a+1
print("----------------------------------------------------------------")


a = 0
while a>-len(t):
    if t[a] == 6 or t[a] == 7:
        print("index of  ", t[a], 'is', a)
    a = a - 1


print("--------------------------------------------------")


t =(6,5,4,3,4,6,7,4,32,7,6,7,6,42,8,5,7,6,4,6,6,6,6,6,643,2,34,2,12,7,7,77,5,43,6,7,7,6,5,56,5,6,6)
a = -1
while a >= -len(t):
    if t[a] == 6 or t[a] == 7:
        print('index of ', t[a],a)
    a = a-1

print("==-----------=======================------------------------")

d ={'k1': "sudh", "k2": "kumar", "k3": (2,3,4,56,6)}
a = 0
b = list(d.keys())
while a < len(d):
    print(d[b[a]])
    a = a+1
print("______________________________________________________")


"""
len()
range()
print()
keys()
values()
items()
append()
pop()
insert()
extend()"""  # these are in build functions




# interduction of a function



def test():
    l = (1,2,3,4,5,6,7,8,9,0)
    a = 0
    while a < len(l):
        print(l[a])
        a = a + 1
print(test())
print("-------------------------------------------------")

def test1():
    print("This is my first function")
print(test1())


print("------------------------------------------------------")

def test2():
    print("This is my first function")
print(test1())

print("-------------------------------------------------------------")

def test3():
    return "this is my first function"

print(test3())
print(type(test3()))
print(test3() + " ", "naveen")

print("________________________________________")

def test4():
    pass

print("----------------------------------------------------------------")




def test4():
    return 1,2,3,4,5,6,[1,2,3,4,6,7,8]

print(test4())

print("================================================================")

a,b,c,d,e,f,g = test4()

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

def test5():
    a = 4*5
    b = 6+4
    return a,b

print(test5())
print("--------------------------------------------------")
g = test5()

print(g)

print("------------------------------------------")

_, m = test5()

print(_)
print(m)

print("========================================================")

# _ is known as place holder


print(g)

print("-----------------------------------------")


def con():
    a = 1
    b = 10
    while a < b:
        print(a)
        if a == 7:
            break
        a = a + 1
    else:
        print("print this")

print(con())


print("*********************************************************************************")



def test6():
    a = 0
    b=  10
    while a<=b:
        print(a)
        a = a+1
    else :
        print("print this else block")

print(test6())


print("-------------------------------------------------------------------------------------------")


def test7(a,b):
    l= []
    while a< b:
        #print(a)
        l.append(a)
        a = a+1
    else:
        print("print this else block")
    return l

print(test7(1,10))

print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")


l = [1,2,34,5,6,7,8,2,1,343,3,2,45,6,8,9,[3,4,5,6,7,8,9,21,7,7],"sudh"]

def list():
    l1 = []
    for i in l:
        if type(i) == int:
            l1.append(i)
    return l1

print(list())


print("*******************************************************************************")
l3 = [2,3,234,345,23,323,3,"naveen", (4,5,6,7,8)]

def list1(l):
    l1 = []
    for i in l:
        if type(i) == int:
            l1.append(i)
    return l1

print(list1(l3))

print("--------------------------------------------------------------------------")


t = (1,2,3,4,5,7,8,9,0,26,7,8,6,3,5,8,9,6,4,6,54,6,7,7,75,6,6,3,4,57,4)

def test9():
    a = -1
    while a >= - len(t):
        if t[a] == 6 or t[a] == 7:
            print("index of ", t[a], a)
        a = a - 1

print(test9())


print("************************************************")

def test9(t):
    a = -1
    while a >= - len(t):
        if t[a] == 6 or t[a] == 7:
            print( "index of ", t[a], a)
        a = a - 1

print(test9((3,4,5,6,7,8,93,5,6,7,3,4,56,6,6,7)))


