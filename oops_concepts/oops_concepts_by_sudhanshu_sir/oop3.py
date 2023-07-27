class person1:
    def __init__(pycham, name, surname, email_id, day_of_birth):
        pycham.name1 = name             #
        pycham.cup = surname
        pycham.mug = email_id
        #pycham.jug = day_of_birth

    def __init__(pycham, name, surname, email_id, day_of_birth):
            pycham.name1 = name  #
            pycham.cup = surname
            pycham.mug = email_id
           # pycham.jug = day_of_birth

    def __init__(pycham, name, surname, email_id, day_of_birth):
                pycham.name1 = name  #
                pycham.cup = surname
                pycham.mug = email_id
                pycham.jug = day_of_birth

    def age(pycham, current_year):
        return current_year - pycham.jug  # we have to return the values with the attribute_name only!!!!!! jug is the attribute name for year_of_birth

iphone = person1("sainaveen","Adep","1234@gmail.com", 1999)
android = person1("naveen", "kumar", "kumar@gmail.com",1994)
print(iphone.age(2022))

s = "hare"
print(s.upper()) # in the same way we are using age variable here


print("*********************************************************")




class person:
    def age(self, current_year, year_of_birth):
        baba = input("enter your date of birth once again it will show your age")
        return baba

    def email_id_input(self, email_id):
        print("take and mail id from a person and print it", email_id)
    def ask_name(self):
        name = input("tell me your name")
        return name
    def ask_dob(self):
        dob = input("tell me your date of birth")
        return dob


hare = person()
krishna = person()
rama = person()
govinda = person()

hare.email_id_input("harekrishna@golokam.com")
print(hare.ask_name())
print(govinda.ask_dob())
print(govinda.age())