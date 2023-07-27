#from test2 import person2,sudh
from utils.utils1 import car, off_roader_var, naveen

print()

class person1:
    def __init__(self, name, surname, yob):
        self.name = name
        self.surname = surname
        self.yob = yob

krishna_var = person1('naveen', 'Adep', '1996')
#print(sudh._name)
#print(sudh._person2__surname)
print('this a car variable that is imported from utils.utils1:  ',car)
print('Name of a off_roader brand', off_roader_var.Brand)
print('Name of a off_roader vehicle', off_roader_var.nameOfACar)
print(naveen._name)
print(naveen._person2__surname)