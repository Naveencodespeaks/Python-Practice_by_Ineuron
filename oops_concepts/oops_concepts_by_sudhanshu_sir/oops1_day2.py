import logging
import oops_day2        # we can use the code in one file in the another file by using import and the file name
print(oops_day2)
logging.basicConfig(filename="oops_day2", level=logging.DEBUG, format=("%(message)s"))

obj3 = oops_day2.person1("naveen", "Adep", 1886)            # we can also use the objects in the file by writing  file name and the object name
# press ctrl and click right  on the person1 object then you will  go to that oops_day2 file
print(obj3.yob1)
print(obj3._name123)
print(obj3._person1__surname321)

class person:

    _name = "naveen"
    __surname = "Adep"
    yob = 1996

    def _age(self, current_year):
        return current_year - self.yob

    def __age1(self, current_year):
        return current_year - self.yob


obj = person()
print(obj._age(2022))
print(obj._person__age1(2022))

class employee(person):
    _name = "srikanth"
    __surname = "ADEPU"
    yob = 1990


obj1 = employee()
print(obj1)
print(obj1._person__age1(2022))
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)
print(obj1._name)





