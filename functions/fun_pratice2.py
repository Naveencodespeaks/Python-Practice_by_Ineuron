def test(a,b):
    return a +b

print(test(4,5))
print(test("hare", "krishna"))

print(test(a =20, b= 40))

print(test(b= 40, a =32))

def test1(a,b,c,d,e):
    return a,b,c,d,e

print(test1(3,4,5,6,7))
#print(test1(3,4,3,2))  # this line of code through you an error because  i have passed only 4 arguments instered of 5

def test(*a): # we can provide n number of of values into it there will be no error because we are using * symble
    return (a)

print(test(1,2,3,4,5,6,4))
print(test(9,8,76,5,4,3,2,52,5,13,2,3,5,1,466,463))

def test5(*a):
    l =[]
    for i in a:
        l.append(i)
    return l
print(test5(2,22,24,5,3,5,23,6235,32,4,2153,))

def test6(a,b,c,d,*m):
    return a,b,c,d,m

print(test6(3,4,5,34,324,34,1354,322,532,4,35,12,2355,25,324,235,35,3,3,3,221,5,6,3))

def test7(*m,a,b,c,d,e):
    return m,a,b,c,d,e
#print(test7(3,3,2143255,124,34,21,1,1,24464778,8,5,34,45,5,2423,4246,547,4363,32546,6,7))
# this line 37 show you an error because wea re using staric operation at the first and look's for remailing a,b,c,d,e value assiging

print(test7(1,234,235,2,523,5432,5,2446.75674,62,3214,4523532,a=7634,b=532,c=543,d=23,e=5))

def test8(**naveen):
    return naveen

print(test8(b=2,c=32,d=523423,e=353242)) # it's trying to accumulate every thing in an dictionary
"""the output will be in dictonary"""
# because of **

d = {'b': 2, 'c': 32, 'd': 523423, 'e': 353242}
print(test8(d))

