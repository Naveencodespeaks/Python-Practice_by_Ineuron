# Ths is the basic of function
def test(a,b):
    return a+b
print(test(1,3))
print(test("naveen", "Adep"))
print(test(a = 4, b = 40))
print(test(b = 20, a =10))

print("@************************************************************************@")


def testA(a,b):
    '''This is my function for concatination or addition'''    # this is a docstring
    return a+b

print(testA(10,5))

print("---------------------------------------------------------------------------------")

def test1(a,b,c,d,e):
    return a,b,c,d,e

print(3,4,5,6,7)

print("-----------------------------------------------------------------")


def test(*a):
    '''* a means (* of any thing not only a, it can be b or c or your name or my name) {single *}, that i can provide any number of parameter that i am looking for'''
    return a

print(test(9,3,4,5,88,3,234,9))
print(test(2,3,45,2,5,2,4,[2,3,3424,45,1,1,2,323,4]))


print("********************************************************************")

def test4(*args):
    '''Here args is not a keyword it can be your name, my name or anything that you are will to give,it just a parameter'''
    return args

print(test4(1,2,4,[1,2,3,5]))

def test5(*a): #Here a can be any thing your name, my name any thing if u are will to give
    '''Here *a used for multiple parameters at a time'''
    l = []
    for i in a:
        l.append(i)
    return l

print(test5(2,3,4,5,[12,4,5,73,32,4,4]))

print("--------------------------------------------------------------")


def test6(a,b,c,d,e,*m):
    return a,b,c,d,e,m

print(test6(1,2,3,4,56,7,3,2,23,234,54,2,1,3,5,7,34,4,2))
'''Here a,b,c,d,e are going to thanke the values that are provided and remaining values are then my *m'''


print("----------------------------------------------------------------")


def test7(*m,a,b,c,d,e):
    return m, a,b,c,d,e
print(4,5,6,7,4,3)

print("-----------------------------------------------------------------")


def test8(**naveen):
    '''Here Double ** is for keyvalue of n number of input'''
    # This give you the output in the dict mannaer
    return naveen

print(test8(b = 5,c =9, d= 5, e =6))

print("------------------------------------------------------------------------------------------------------------")


def test9(*m, **s):
    '''single * means which give you n  mumbers of varibles in tuples where as ** means which gives you n numbers of variable in dictionary'''
    return m,s

print(test9(34,5324,1234,452,4234,34,2455,667,3,1,431,34,b=9,c=34,d=5,e=32,f=56,i=6))

print("-------------------------------------------------------------------------------------------------")


def test10(*m):
    n = 0
    for i in m:
        if type(i) == int:
            n = n+i
    return n

print(test10(1,2,3,4,5,7,92,34,34,4,2,34,25,5))

print("----------------------------------------------------------------")

def test11(*m):
    n = 1
    for i in m:
        if type(i)==int:
            n = n *i
    return n

print(test11(1,2,3,4,1,33,4,5,2))

print("-----------------------------------------------")

def test11(*n):
    m = 1
    for i in n:
        if type(i)== int:
            m = m-i
    return m

print(test11(1,2,3,44,5,32,1))

print("---------------------------------------------------------------")


n = lambda a, b: a+b
'''lambda is a anonymous  function  function with out a name is called anonymous '''

print(n(4,5))


def test13(a,b):
    return a+b

print(test13(4,5))


print("------------------------------------------------------------------")

b = lambda *sudh : sudh

print(b(2,3,4,5,721,12,3,412,4,5,7,34,1))

print("*************************************************************************")
'''comprehensive operations'''


t = (1,2,3,4,2,3,34,5,78,1)
l = []
for i in t:
    l.append(i)

print(l)
'''list comprehensive operations'''
print([i for i in t])


print("*******************************************")

s = "naveen"

print([i for i in s])

print([i*i for i in range(10)])
"""we can perform the same code in different ways"""
l =[]
for i in range(10):
    l.append(i*i)

print(l)

print("--------------------------------------------------------------------------")

l = lambda *x :[i for i in x]
print(l(4,5,6,77,89,1,2,3,45,7))

print("----------------------------------------------------------------------------------")

l = lambda *x :[i**2 for i in x]
print(l(4,5,6,77,89,1,2,3,45,7))

print("----------------------------------------------------------------------------------")




