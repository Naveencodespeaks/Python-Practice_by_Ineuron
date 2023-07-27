# test5_polymorphism.log

import logging
logging.basicConfig(filename ='test5_polymorphism.log', level = logging.INFO, format ='%(levelname)s %(name)s %(asctime)s, %(message)s')

class ineuron:
    def students(self):
        logging.info("print a students details")

class class_type:
    def students(self):
        logging.info('print the class type of students')


def ineuron_external(a):  # This function is  like bridge to the all the class
    a.students()


i = ineuron()
j = class_type()
ineuron_external(i)
ineuron_external(j)


def test(a,b):
    return a+b

logging.info(test(3,4))
logging.info(test('naveen', ' Adep'))


# These are the concepts we have learnt in OOPS concepts ( Object-oriented programming system)
'''class
object
constructor
inheritance
private
public
protected
abstraction
encaptulations
polymorphism
packages
modules
method overriding'''