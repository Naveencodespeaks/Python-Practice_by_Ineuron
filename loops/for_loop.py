l = [1,2,3,4,5,6,7,8,9,10,"sainaveen", "Adep", 45.98]

for i in l:
    print(i)

print("---------------------------------------")

for i in l:
    pass
print("-------------------------------------------------")

s  = "Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare"
for i in s:
    print(i)


print("-------------------------------------------------------------------")

for i in l:
    print(i)
else:
    print("if for loop is going to complete itself then it will execute else")

print(l)

print("-------------------------------------------------------------------")


for i in l :
    if i == 4:
        break
    print(i)
else:
    print("This will execute only if for is going to complete itself")


print("----------------------------------------")

for i in l:
    if i ==5:
        break
    print(i)
else:
    print("This will execute only if for is going to complete")


print("--------------------------------------")

s = "hare krishna"

for i in s:
    if i == 'n':
        break
    print(i)
else:
    print("print string", s)


print("----------------------------------------------------------")



for i in s:
    if i =='z':
        break
    print(i)

else:
    print("print string", s)

print("-------------------------------------------------")


t = (4,5,6,7,8,9,"hare krishna", "naveen", 45.8)

for i in t:
    print(i)

print("---------------------")

b = {4,5,6,34,235,346,67235,673,557324,"naveen"}
print(type(b))

print("--------------------------------------------------------------------")

print(b)

print("-------------------------------------------------------------------------------")

for i in b:
    print(i)



print("----------------------------------------------------")




d ={'key1': "hare", 'key2': 'contact', 'key3': "naveen", 'contact': 7997137711, 'position': "xyz", 'mail': 'sainaveen@gmail.com'}

for i in d:
    print(i)

print("---------------------------------------------------------------------------------")

for i in d:
    print(d[i])

print("---------------------------------------------------------------------------------")

print(d['key1'])

print(d['key2'])

print(d['position'])


print("---------------------------------------------------------------------------------")


print(range(9))

print("-----------------------------------")

print(list(range(9)))

print("------------------------------------------")


for i in range(9):
    print(i)

print("------------------------------------------------")


print(list(range(0,9)))

print("=--------------------------------------------------")

print(list(range(0,9,2)))

print("*******************************************************")

print(list(range(0,10,-1)))

print("_____________________________________________")

print(list(range(9,0,-1)))


print("===================================================")


n = 4

for i in range(4):
    for j in range(0, i+1):
        print("hare", end="  ")
    print("\n")

print("--------------------------------------------------------")

for i in range(9):
    for j in range(0, i+1):
        print("*", end="  ")
    print("\n")

print("--------------------------------------------------")

for i in range(3):
    for  j in range(i, n-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("naveeen", end =" ")
    print("\n")

print("------------------------------------------------------------")


n = 3

for i in range(n):
    for j in range(i,n-1):
        print(" "*len("naveen"), end = " ")
    for j in range(i +1):
        print("naveen", end=" ")
    for j in range(i):
        print("naveen", end =" ")
    print("\n")

print("-------------------------------------")


t = (3,53,4324,45,23,323,42,43,894,3,11,3,4)

for i in range(len(t)):
    print(i, t[i])


print("---------------------------------------------")

s = "ineuron"

for i in range(len(s)):
    print(i, s[i])

print("------------------------------")
for i in range(len(s)-1,-1,-1):
    print(i, s[i])

print(d)


print("------------------------------")


print(d.items())


print("----------------------------------------------")

t = (2,3,4,5,6,2,4,5,63,3,4,5,2,7,2,5,2)

for i in range(len(t)):
    print(i,t[i])

print("------------------------------------------------------")

print(t[0])
print(t[1])


print("-------------------------------------")

for i in range(len(t)):
    print(i,t[i])


print("-----------------------------------")
s="ineuron"

for i in range(len(s)):
    print(i,s[i])


print("___________________")

for i in range(len(s)-1,-1,-1):
    print(i,s[i])

print("------------------------------------------------------")




print("___________________________________")

l = ["sudh","kumar", 324632,"sudhanshu@ineuron.ai", 345,12423521]
l1 =[]

for i in l:
    if type(i) == int:   # here are we are printing the only integer values
        l1.append(i)

print(l1)

print("------------------------------------------------------------")


d = {1: 32456234,"name":"sudh", "email_id": "sudhanshu@ineuron.ai", 234 : "fsdssf", "2342": "sadtfk",234: "6529"}

for i in (d):
    if type(i) == int:
        print(i, ":", d[i])  # here we are  printing the only the integer values.
print("------------------------------------------------------------------------")


for i in (d):
    if type(i) == str:
        print(i,":", d[i])

print("-----------------------------------------------------------------")


for i in d:
    if type(i)== int:
        print(i, ":", d[i])

print("-----------------------------------------------------------------------")

s = "aaaaabbccd"
for i in set(s): # here we are using the set to get unique values
    print(i, ":", s.count(i))
print("-----------------------------------------------------------------------------")
print(s.count('a'))


print("--------------------------------------------------------------------------------")

i = 3432554732546673143556531254255

for j in str(i):
    print(j)

print("-------------------------------------------------------------------")

for j in str(i):
    print(j, ":", type((j)))

print("---------------------------------------------")


for j in str(i):
    print(j,":", type(int(j)))

print("-----------------------------------------------")

t = ("sudh", "kumar", [1,2,3,42,1,3],(31,41,2,4,3,2,3,2,3254231,32,2,3,3,3,3),{3:3,"key1": "sudh", "key2": "kumar"})
for i in t:
    if type(i)== list or type(i)== tuple:
        for j in i:
            if j == 3:
                print(j)
    if type(i) == dict:
        for k,v in i.items():
            if k == 3 or v == 3:
                print(k)
                print(v)
print("---------------------------------------------------------------")

d = {4:5, "key1":"sudh", "key2": "naveen", "key3": "hare"}

for i in d.items():
    print(i)


print("------------------------------------------------------------------------")
a = 10,
b = 20,
c = 30,

print(a,b,c)

a,b,c = 10,20,30

print(a,b,c)

a,b,c = (10,20,30)

print(a,b,c)


print("-------------------------------------------------------------")






