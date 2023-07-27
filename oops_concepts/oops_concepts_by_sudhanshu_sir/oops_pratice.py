class person:
    def __init__(self, name, surname, email_id, year_of_birth): # self is a pointer to the class!!!!!
        self.name = name                                      # self can be written as anything your name my name or someone else name!!!!!
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth =year_of_birth  # here name = name, surname = surname , email_id= email_id, year_of_birth = year_of_birth are not same

krishna_var = person("krishna","hare","krihsna@golokam.com",1996)
sudh = person("sudhasnshu","kumar", "sudhanshuu@gmail.com", 1993)
gargi = person("gargi", "kumari","gargi@gmail.com",1999)
xyz = person("xyz", "zyx", "xyz@gmail.com", 1234)
print(krishna_var.name)
print(krishna_var.surname)
print(krishna_var.email_id)
print(krishna_var.year_of_birth)
print("*****************************************************************")
print(sudh.name)
print(sudh.email_id)
print(gargi.name)
print(gargi.email_id)
print("*******************************************************************")
print(xyz.name)
print(xyz.email_id)
print(xyz.year_of_birth)
print(xyz.surname)

print("*******************************************************************")


print("This is an example for showing the name and self and variable are different")
class person:
    def __init__(pycham, name, surname, email_id, year_of_birth):
        pycham.name1 = name             # here name1, cup, mug, jug are called attributes
        pycham.cup = surname
        pycham.mug = email_id
        pycham.jug = year_of_birth

    def age(pycham, current_year):
        return current_year - pycham.jug  # we have to return the values with the attribute_name only!!!!!! jug is the attribute name for year_of_birth

iphone = person("sainaveen","Adep","1234@gmail.com", 1999)
android = person("naveen", "kumar", "kumar@gmail.com",1994)
print(iphone.age(2022))
print(iphone.name1)
print(iphone.cup)
print(iphone.mug)
print(iphone.jug)
print("***************************************************************")
print(android.name1)
print(android.cup)
print(android.mug)
print(android.jug)

print(iphone.name1 + iphone.cup)

s = "Hare Krishna"
s1 ="Hare Rama"


print(s + " "+s1)
print(type(s+s1))

print("******************************")
s = "hare"
print(s.upper())

print("***************************************************")



