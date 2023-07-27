class person1:
    def __init__(pycham, name, surname, email_id, day_of_birth):
        pycham.name1 = name             #
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