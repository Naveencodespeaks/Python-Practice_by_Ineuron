import OOPS_SUDH # here we are importing the OOPS_SUDH file and performing variable operation with different obj3
print(OOPS_SUDH)
obj3 = OOPS_SUDH.Person1("sudh",'kumar','sudhandhu@ineuron.ai', 1996, 5)
print(obj3.year_of_birth)
print(obj3.surname)
print(obj3.email_id)
class person2:
    _name =  'sudh'
    __surname = 'kumar'
    yob = 1996

sudh = person2()
print(sudh._name)
print(sudh._person2__surname)

