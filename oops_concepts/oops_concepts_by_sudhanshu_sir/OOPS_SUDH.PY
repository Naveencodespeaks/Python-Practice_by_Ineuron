import logging
logging.basicConfig(filename= "oopsTest.log", level = logging.INFO , format=' %(levelname)s %(asctime)s   %(name)s %(message)s')

#___________________OOPS_____________________________

print('@__________________OOPS_______________________@')
logging.info("#____________oops concept__________________________________________")

class Person:
    pass
logging.info('init is the  initialization of a particular variable to a classes , is known as constructor')
# when ever you write the init use, __init__
# __init__ is the  initialization of a particular variable to a classes , is known as constructor


# here self is a pointer to the class!!!
# At any point of a time the very first variable in the class function in side a python is known as a pointer, pointing to the particular class

# here "self" is not a keyword it can be your name, my name or any_thing that you wish it can be writen.
class Person1:
    def __init__(self, name, surname, email_id, year_of_birth, height):
        self.name = name
        self.surname = surname
        self.email_id = email_id
        self.year_of_birth = year_of_birth
        self.height = height

# where_as self.name = name is not the same, where self.name  is  called class variable
# where_as name is "Allocations or reference or assignments operation to a class variables
    def age(self, current_year):
        return current_year - self.year_of_birth


anuj_var = Person1('anuj', 'bandari', 'anuj@gmail.com', 1996, '5.9' )
logging.info(anuj_var.name)
logging.info(anuj_var.surname)
logging.info(anuj_var.email_id)
logging.info(anuj_var.year_of_birth)
logging.info(anuj_var.height)
logging.info(anuj_var.age(2022))



logging.info("______details of the car_____________________________")

class car:

    def __init__(self, Brand, nameOfACar, model, price, variant):
        self.Brand = Brand
        self.nameOfACar = nameOfACar
        self.model = model
        self.price = price
        self.variant = variant

# here off_roader_var, suv_var, seden_var are the class variable
logging.info('# here off_roader_var, suv_var, seden_var are the class variable')

off_roader_var = car('Force', 'Gurkha', '4WheelDrive', '14,00,00/-','TopEnd')
suv_var = car('Mahendra', 'xuv500', 'W10', '22,00,00/-','Diesel')
seden_var = car('Maruthi', 'ciaz', 'Alpha', '8,99,500', 'Petrol')
logging.info(off_roader_var.Brand)
logging.info(off_roader_var.nameOfACar)
logging.info(off_roader_var.model)
logging.info(off_roader_var.price)
logging.info(off_roader_var.variant)
logging.info("_______information about suv car__________")
logging.info(suv_var.Brand)
logging.info(suv_var.nameOfACar)
logging.info(suv_var.model)
logging.info(suv_var.price)
logging.info(suv_var.variant)
logging.info("_______information about suv car__________")
logging.info(seden_var.Brand)
logging.info(seden_var.nameOfACar)
logging.info(seden_var.model)
logging.info(seden_var.price)
logging.info(seden_var.variant)
logging.info(type(suv_var))
logging.info("#______Here we are performing concatenation operation_________")
logging.info(suv_var.Brand + " " + suv_var.nameOfACar) # we can perform concatenation operation
logging.info("---------------------------------------")


logging.info('This is the basic information for concatenation operation')
s = "naveen"
s1 = "Adep"
logging.info(s + " " + s1 )




