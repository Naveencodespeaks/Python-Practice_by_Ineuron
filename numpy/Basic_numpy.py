import numpy as np

l = [1,2,3,4,5]

print(np.array(l))

l1 = [4,5,6,7,8, "naveen", 34.5345, True]

a1 = np.array(l1)# which converted each and every thing into string
print(a1)
a2 = np.array([[1,2,3,],[4,5,6,]])
print(a2)
a3 = np.array([[[1,2,3],[1,3,4], [4,5,6]]])
print(a3)
print("This is a1 array dimension : ",a1.ndim) #ndim is known as  dimension array
print("This is a2 array dimension : ",a2.ndim)
print("This is a3 array dimension : ",a3.ndim)

print("This give us how many elements are there in a1 array: ",a1.size)
print("This give us how many elements are there in a2 array: ",a2.size)
print("This give us how many elements are there in a3 array: ",a3.size)


print('This gives shape of the matrix of a1:',a1.shape)
print('This gives shape of the matrix of a2:',a2.shape)
print('This gives shape of the matrix of a3:',a3.shape)  # we have to read the following matrixes as 3 cross 3 and 1 such kind of matrix



print("it generate random numbers between 2 to 10: ",np.random.randint(2,10)) # it generate random numbers between 2 to 10
print("it generate random numbers between 2 to 100: ",np.random.randint(2,100)) # it generate random numbers between 2 to 100

print("it will generate the data between 2 to 50 like  3 rows and 4 columns:\n ",np.random.randint(2,50,(3,4))) # it will generate the data between 2 to 50 like  3 rows and 4 columns

print("it will generate the data between 2 to 50 like  3 rows and 4 columns:\n ",np.random.randint(2,50,(2,3,4))) # it will generate the data between 2 to 50 like  3 rows and 4 columns


print(np.random.rand(2,3))

print(np.random.randn(2,5))


a4 = np.random.rand(4,4)
print(a4)

print(a4.reshape(2,8))

print(a4.reshape(8,2))
print(a4.reshape(16,1))
print(a4.reshape(2,-1))

print(a4.reshape(2,2,4))


print(a1)
print(a1[0])
print(a1[2:6])


print(a1[2:6:2])

print(a1[::-1]) # which means it reverse entire list


print(a2)

print(a2[:,1:])

print(a2[[0,1],1:])

print(a2[[0,1],1:])

print(a2[:,[1,2]])

a5 = np.random.randint(2,90,(6,5))
print(a5)

print(a5[a5>40])

print(a5)

print(a5[0,1])
# a5[0,1] = 100 we can change the value of 0th row and 1st column to 100 it rowing in jupyter notebook  not working in pychamp
print('----------------------------')
a6 = np.random.randint(0,3,(3,3))
print(a6)

a7 = np.random.randint(0,3,(3,3))
print(a7)
print("-------------------------------")
print(a6*a7)  # this is element wise multipication

print('---------------------')

print(a6@a7) # this is matrix maltipication
print("------------------")
print(a6)
print(a6+100)
print("------------")
print(a6*2)
print("------------")
#print(a6/0) # in numpy we have a values for infinity and it don't through you an error  but gives you a warring!
print(a6)

print(a6**3) # this gives power operation of 3

print("-------------------------")

a8 = np.zeros((4,4))
print(a8)
print("---------------")
a9 = np.ones((4,5))
print(a9)
print("---------------")
print(a9+10)
print("-------------------")
print(a9 +np.array([1,2,3,4,5])) # it performing row wise  addition operation
print("compari with:",a9 +np.array([1,2,3,4,5]))
print("---------------")
print(a9,'# it performing row wise  addition operation')
print('-------------')
print(a9,'This type of operation is known as broadcast operations')
print(a9+np.array([1,2,3,4,5]))
print("------------")
print(a9)

print(np.array([1,2,3,4]))
print("-----------")
print(np.array([[1,2,4,6]]).T) # This is transpose operations
print("---------------------")
print(np.array([[1,2,4,6]]).T+a9)

print(a6)
print("------------------")
print(a6.T, "This is the transpose of a6 ")

print(a5)

print(np.sqrt(a6),"--------------This is the sqaureroot of array a6")
print(np.exp(a5),"---------------------This is the exponent of array a5")
print(np.log10(a5), "--------------------This is the log of an array a5")
print("-----------------")
print(list(range(0,10,2)))
#print(list(range(10,3,7.5)))# we cannot perform the flotingpoint in range function
print('print(list(range(10,3,7.5)))# we cannot perform the flotingpoint in range function')
print("------------")
print("-------------")
print(np.arange(10))
print("-------------")
print(np.arange(1.8,10.7,2.5),"In numpy we can perform the floating point range function")
print(np.linspace(2,3,num =50))
print("-------------")
print(np.linspace(2,3, num = 50, retstep= True))
print("-------------")
print(np.logspace(2,4, num =4, base = 10))
print("---linespace and  logspace are same but linespace consider the linear space  and logspace consider the logorithamic one-----")

print(np.eye(5), "This is an identity matrices")

