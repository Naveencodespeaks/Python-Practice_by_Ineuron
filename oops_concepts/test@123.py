import logging
logging.basicConfig(filename = 'Inheritance_oops_day2_test2.log', level = logging.INFO, format = '%(name)s  %(levelname)s %(asctime)s %(message)s')


# with out using __init__ we can able to create a variable
logging.info('________________with out using __init__ we can able to create a variable________________________________')
# if we are using __init__ method  we have to pass the data in the __init__
# now without using the __init__ function we can able to create a variable
class person:
    # global variable's
    _name = "sudh"
    __surname = "kumar"
    yob = 1990

obj = person()
logging.info(obj)
logging.info('#________________inheritance_______________________')

''' here employee is child class
# and person is known as parent class'''

class employee(person):# Here we have created employee class and trying to call person class  # This is called "inheritance"
    #pass
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991
# here we are over_riding the object values
obj1 = employee()
logging.info(obj1)
logging.info(obj1.yob)
'''no where in the employee class we have declared yob but  still we can able to execuite yob,
    here yob is decliraed in the person class so we have inheriting the person class to child class '''
logging.info(obj1.yob)
logging.info('This is a private variable: %s',obj1._name)
logging.info('This is a private variable:  %s', obj1._person__surname)
logging.info('This is a private variable:  %s',obj1._name)
logging.info('This is a private variable:  %s',obj1._person__surname)
logging.info('This is a private variable:  %s',obj1._employee__surname)


logging.info('@@---------------------------Here we are using functions as a object notations---------------------------------------------------@@')
# 'Here we are using functions as a object notations'
class person:
    # global variable's
    _name = "sudh"
    __surname = "kumar"
    yob = 1990

    def _age(self, current_year):
        return current_year - self.yob

    def __age1(self,current_year):
        return current_year - self.yob

obj = person()
logging.info('Here the age is protected: %s', obj._age(2022))
logging.info('Here The age is private %s', obj._person__age1(2022))

# In the same way we use to call object same in function  are also called by using _age(), _person__age1()

logging.info('___________________________________________________________________________________________________________________')

# here i have coped and pasted the code from line number 22 to 38
logging.info('@----------here i have coped and pasted the code from line number 22 to 38--------------------@')

class employee(person):# Here we have created employee class and trying to call person class  # This is called "inheritance"
    #pass
    _name = "sudhanshu"
    __surname = "singh"
    yob = 1991
# here we are over_riding the object values
obj1 = employee()
logging.info(obj1)
logging.info(obj1.yob)
'''no where in the employee class we have declared yob but  still we can able to execuite yob,
    here yob is decliraed in the person class so we have inheriting the person class to child class '''
logging.info(obj1.yob)
logging.info('This is a private variable: %s',obj1._name)
logging.info('This is a private variable:  %s', obj1._person__surname)
logging.info('This is a private variable:  %s',obj1._name)
logging.info('This is a private variable:  %s',obj1._person__surname)
logging.info('This is a private variable:  %s',obj1._employee__surname)
logging.info(obj1._age(2000)) # here we are performing the function operation to get the protected operations
logging.info(obj1._person__age1(2022)) # here we are performing the function operation to get the private  operations from different classes

