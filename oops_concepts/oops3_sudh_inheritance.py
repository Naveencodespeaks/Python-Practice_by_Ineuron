# inheritance
import logging
logging.basicConfig(filename ='oops3_sudhanshu_inheritance.log', level = logging.INFO, format ='%(levelname)s %(name)s %(asctime)s, %(message)s')


class car:
    def __init__(self, body,engin, tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage(self):
        logging.info("milage of this car")


c = car('solid', 'v6', 'radial')
logging.info(c)
logging.info('Here we are telling about body of a car %s', c.body)
logging.info(c.engin)
logging.info(c.tyre)


class tata(car): # This inheritance passing car class into tata class
    pass

# from line 27 and 28 gives you an  TypeError: car.__init__() missing 3 required positional arguments: 'body', 'engin', and 'tyre'
# because you have not passed values in the tata() class
'''t = tata()                         # object is noting but variable of particular class, here t is a variable but it also an object to the tata class()
logging.info(t)'''

t = tata('solid', 'v8', 'radial')
logging.info(t)
logging.info(t.engin)
logging.info('Here we are telling about body of a car: %s',t.body)
logging.info(t.tyre)

logging.info(t.milage())