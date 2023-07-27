
'''Basic file operation, Generator,map, Reduce, Filter'''

l = [1,2,3,4,5,6,7]

for i in l:
    print(i)

# next(l)
'''nature of next function is that it try to extract the information one by one one by one and then try to give it to u'''


print("--------------------------------------------------------------------------")
b = iter(l)
print(next(b))
print("--__________----------------____________------------_______________--------------")
print(next(b))
print("************************************************************************************")
print(next(b))
print("----***********-----------------************************----------------------**********")

# iterator and iterable

print(l)

'''List elements are by defalut are iterable'''

'''By defalut list object are iterable object '''
'''for loop internatlly trying to call and then it trying to call next function '''

'''When it trying to call (iter) function so it is trying to convert iterable into iterator'''
'''Then with the help of next function it will try to extract the data one by one one by one and give it to you!!!!!'''

'''if some object are not iterable then you will not able to convert it into iterator'''
# Example:
# """for i in 43456:
#   print(i)"""


for i in l:
    print(i)

# defination:-  if objects are iterable for loop try to convert all those object into iterator, and by appliong next() function then it will start  extracting the data then i will be able to get an information
# its is now for loop is going to work.!!!!!



s = "Hare krishna"

#next(s)


#  @@ important @@

# By default strings are not iterator object but
# By default strings are iterable object.

print("--------------------------------------------------------------------------------------")
s1 = iter("Hare krishna")

print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")


s2 = "Hare krishna"
for i in s2:
    print(i)

# Note:  internally for loop is using length function,iter function, and next function
# length() function where to stop
# iter() function to convert any iter variables into iterators
# next() function to call the data next(), next(),next(), one by one to show you the data at any point of a time

print("********************************************************************")


t = (5,6,7,8,9,2,4,9)

t = iter(t)

for i in t:
    print(i)


print("****************************  From this we are going to work on ******************************")


print(range(1,10))

print("********************************************************************")

print(list(range(0,10)))

print("********************************************************************")

def square_fun(n):
    x = [i*i for i in range(n)]
    return x

print(square_fun(10))

print("-----------------------------------------------------------------")


def square_fun(n):
    x = [i*i for i in range(n)]
    yield x

print(square_fun(10))


for i in square_fun(4):
    print(i)
print("--------------------------------------------------")



def generatefib(n):
    a = 1
    b = 1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b, a+b
    return l
print(generatefib(10))



def genfib(n):
        a = 1
        b = 1
        l = []
        for i in range(n):
            l.append(a)
            a,b = b, a+b
        print(l)
print(genfib(30))

print("-----------------------------------------------------------")


def genfib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a +b
print(genfib(30))


for i in genfib(10):
    print(i)

# file operation


f = open("Range Rover.txt",'w')
f.write("This is my very first file operation")
f.close()
print("----------------------------------------------------------")

f1 = open("Range Rover Evoque.txt",'w')
f1.write("Land Rover Range Rover Evoque 2.0 R-Dynamic SE Price \n Ex-Showroom PriceRs.72,09,000 \n RTORs.7,20,900 \n InsuranceRs.3,07,219 \n Others Rs.72,090 \n On-Road Price in New DelhiRs.83,09,209*")
f1.close()


f2 = open("Tata Harrier.txt",'w')
f2.write("XT plus Dark Edition(Diesel) \n Ex-Showroom PriceRs.18,54,900\n RTORs.3,15,333\n InsuranceRs.1,00,752\n OthersRs.18,549\n On-Road Price in Hyderabad :Rs.22,89,534*")
f2.close()


l = [1,2,3,4,5,6,7,89,7,9]
f3 = open("list.txt",'w')
f3.write(str(l))
f3.close()


"""f4 = open("Royal Enfield.txt",'w')
f4.write("Ex-showroom (Hyderabad)2,17,588, \n RTO  27,605, \n Insurance (Comprehensive)₹16,144, \n RSA (Road Side Assistance) 1,500, \n On-road  in priceHyderabad, \n  2,62,834*")
f4.close()"""

f=open("Range Rover.txt")
print("read(), which reads the entire thing and display you: ",f.read())
print("seek(), seek help us to relocate the pointer at the starting point: ",f.seek(0))
print("read(), which reads the entire thing and display you: ",f.read())
print("seek(), seek help us to relocate the pointer at the starting point:",f.seek(4))
print("read(), which reads the entire thing and display you: ",f.read())
print('--------------------------------------------------------------------------------------------')

f1 = open("Range Rover Evoque.txt")
print("tell(), tells that where the pointer is located at what point: ",f1.tell())
print("read(), which reads the entire thing and display you: ",f1.read())
print("tell(), tells that where the pointer is located at what point: ",f1.tell())

f2=open("Tata Harrier.txt")
print(f2.read(15))
print("readline(), only read one line: ",f2.readline())
print("readlines(), which read the entire lines in the present file:",f2.readlines())

f1 = open("Range Rover Evoque.txt", 'a')
# a is known as append mode
# append mode in which the it add some thing to the file without removing the previous one in the text
f1.write("\n Tata punch is the car that have scored 5 star rating ")
f1.close()

print("---------------------------------------------------------------------------")
print("# map, reduce, filter")
# map, reduce, filter

print("sqarure of a numbers of a list")
l =[2,3,4,5,6,7]
l1=[]
for i in l:
    l1.append(i**2)

print(l1)

# map
print("#map")


def sqr(n):
    return n**2

print(list(map(sqr,l)))
print("#lambda function")
print((map(lambda x: x**2, l)))


print(list(map(lambda x : str(x), l)))


def str_c(n):
    return str(n)

print(list(map(str_c,l)))


# reduce

print("# reduce")

'''Reduce is a functional tool from that you have to import  reduce python donot have reduce function'''

from functools import reduce


l =[1,2,3,4,5,6,3,23,21,1,24,4,32]

print(sum(l))
print("# using reduce function")
print(reduce(lambda a,b:a+b,l))
print("# using reduce function")
print(reduce(lambda a,b:a*b,l))


#filter
print("#filter")

print(list(filter(lambda x : x%2==0 , l)))


print("# using filter fumction")
def check_even(n):
    if n%2 == 0:
        return True

print(list(filter(check_even,l)))
'''Basic file operation, Generator,map, Reduce, Filter'''

l = [1,2,3,4,5,6,7]

for i in l:
    print(i)

# next(l)
'''nature of next function is that it try to extract the information one by one one by one and then try to give it to u'''


print("--------------------------------------------------------------------------")
b = iter(l)
print(next(b))
print("--__________----------------____________------------_______________--------------")
print(next(b))
print("************************************************************************************")
print(next(b))
print("----***********-----------------************************----------------------**********")

# iterator and iterable

print(l)

'''List elements are by defalut are iterable'''

'''By defalut list object are iterable object '''
'''for loop internatlly trying to call and then it trying to call next function '''

'''When it trying to call (iter) function so it is trying to convert iterable into iterator'''
'''Then with the help of next function it will try to extract the data one by one one by one and give it to you!!!!!'''

'''if some object are not iterable then you will not able to convert it into iterator'''
# Example:
# """for i in 43456:
#   print(i)"""


for i in l:
    print(i)

# defination:-  if objects are iterable for loop try to convert all those object into iterator, and by appliong next() function then it will start  extracting the data then i will be able to get an information
# its is now for loop is going to work.!!!!!



s = "Hare krishna"

#next(s)


#  @@ important @@

# By default strings are not iterator object but
# By default strings are iterable object.

print("--------------------------------------------------------------------------------------")
s1 = iter("Hare krishna")

print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")
print(next(s1))
print("****************************************************************")


s2 = "Hare krishna"
for i in s2:
    print(i)

# Note:  internally for loop is using length function,iter function, and next function
# length() function where to stop
# iter() function to convert any iter variables into iterators
# next() function to call the data next(), next(),next(), one by one to show you the data at any point of a time

print("********************************************************************")


t = (5,6,7,8,9,2,4,9)

t = iter(t)

for i in t:
    print(i)


print("****************************  From this we are going to work on ******************************")


print(range(1,10))

print("********************************************************************")

print(list(range(0,10)))

print("********************************************************************")

def square_fun(n):
    x = [i*i for i in range(n)]
    return x

print(square_fun(10))

print("-----------------------------------------------------------------")


def square_fun(n):
    x = [i*i for i in range(n)]
    yield x

print(square_fun(10))


for i in square_fun(4):
    print(i)
print("--------------------------------------------------")



def generatefib(n):
    a = 1
    b = 1
    l = []
    for i in range(n):
        l.append(a)
        a,b = b, a+b
    return l
print(generatefib(10))



def genfib(n):
        a = 1
        b = 1
        l = []
        for i in range(n):
            l.append(a)
            a,b = b, a+b
        print(l)
print(genfib(30))

print("-----------------------------------------------------------")


def genfib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a +b
print(genfib(30))


for i in genfib(10):
    print(i)

# file operation


f = open("Range Rover.txt",'w')
f.write("This is my very first file operation")
f.close()
print("----------------------------------------------------------")

f1 = open("Range Rover Evoque.txt",'w')
f1.write("Land Rover Range Rover Evoque 2.0 R-Dynamic SE Price \n Ex-Showroom PriceRs.72,09,000 \n RTORs.7,20,900 \n InsuranceRs.3,07,219 \n Others Rs.72,090 \n On-Road Price in New DelhiRs.83,09,209*")
f1.close()


f2 = open("Tata Harrier.txt",'w')
f2.write("XT plus Dark Edition(Diesel) \n Ex-Showroom PriceRs.18,54,900\n RTORs.3,15,333\n InsuranceRs.1,00,752\n OthersRs.18,549\n On-Road Price in Hyderabad :Rs.22,89,534*")
f2.close()


l = [1,2,3,4,5,6,7,89,7,9]
f3 = open("list.txt",'w')
f3.write(str(l))
f3.close()


"""f4 = open("Royal Enfield.txt",'w')
f4.write("Ex-showroom (Hyderabad)2,17,588, \n RTO  27,605, \n Insurance (Comprehensive)₹16,144, \n RSA (Road Side Assistance) 1,500, \n On-road  in priceHyderabad, \n  2,62,834*")
f4.close()"""

f=open("Range Rover.txt")
print("read(), which reads the entire thing and display you: ",f.read())
print("seek(), seek help us to relocate the pointer at the starting point: ",f.seek(0))
print("read(), which reads the entire thing and display you: ",f.read())
print("seek(), seek help us to relocate the pointer at the starting point:",f.seek(4))
print("read(), which reads the entire thing and display you: ",f.read())
print('--------------------------------------------------------------------------------------------')

f1 = open("Range Rover Evoque.txt")
print("tell(), tells that where the pointer is located at what point: ",f1.tell())
print("read(), which reads the entire thing and display you: ",f1.read())
print("tell(), tells that where the pointer is located at what point: ",f1.tell())

f2=open("Tata Harrier.txt")
print(f2.read(15))
print("readline(), only read one line: ",f2.readline())
print("readlines(), which read the entire lines in the present file:",f2.readlines())

f1 = open("Range Rover Evoque.txt", 'a')
# a is known as append mode
# append mode in which the it add some thing to the file without removing the previous one in the text
f1.write("\n Tata punch is the car that have scored 5 star rating ")
f1.close()

print("---------------------------------------------------------------------------")
print("# map, reduce, filter")
# map, reduce, filter

print("sqarure of a numbers of a list")
l =[2,3,4,5,6,7]
l1=[]
for i in l:
    l1.append(i**2)

print(l1)

# map
print("#map")


def sqr(n):
    return n**2

print(list(map(sqr,l)))
print("#lambda function")
print((map(lambda x: x**2, l)))


print(list(map(lambda x : str(x), l)))


def str_c(n):
    return str(n)

print(list(map(str_c,l)))


# reduce

print("# reduce")

'''Reduce is a functional tool from that you have to import  reduce python donot have reduce function'''

from functools import reduce


l =[1,2,3,4,5,6,3,23,21,1,24,4,32]

print(sum(l))
print("# using reduce function")
print(reduce(lambda a,b:a+b,l))
print("# using reduce function")
print(reduce(lambda a,b:a*b,l))


#filter
print("#filter")

print(list(filter(lambda x : x%2==0 , l)))


print("# using filter fumction")
def check_even(n):
    if n%2 == 0:
        return True

print(list(filter(check_even,l)))

