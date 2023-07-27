import logging
logging.basicConfig(filename = 'oop_day2_test1.log', level=  logging.INFO, format= '%(name)s %(levelname)s  %(asctime)s  %(message)s ')

logging.info('@______________________pubic, private, protected___________________________________________________________@')
class person():
    def __init__(self, name, emaild, surname, yob):
        self._name1 = name  #Here _name1 is a protected notation
        self.__emailid2 = emaild  #Here __emailid2 is a private notation
        self.surname3 = surname
        self.yob4 = yob

naveen = person('Krishna', 'krishna@golokham.com', 'Edukula', 3228)
logging.info(naveen._name1)
logging.info(naveen.surname3)
logging.info(naveen._person__emailid2) # if you wnat to call the private one you have to use _classaname and __ variable name EX: print(naveen._person__emailid) or logging.info(naveen._person__emailid)
logging.info(naveen.yob4)


# public
# private: Here just a notation (_) which exist only in python
# protected: Here just a notation (__) which exist only in python

# creator of PYTHON said that there is a public, private, protected variable's in python  but they don't exist

# it's depend up on us to respect other privacy and when to use it and where to use it python!!!!!!

# in python public, private and protected is just a notation!!!!!

class food():
    def __init__(self, pizza, burger, biryani, paneer_puff):
        self.pizza1 = pizza
        self.burger2 = burger
        self.biryani3 = biryani
        self.paneerpuff4 = paneer_puff

food_itmes = food('Cheeses_pizza', 'Maharaja_American_cheese_paneer_burger', 'paneer_fried_biryani', 'panner_stuffed_puff')
logging.info(food_itmes.pizza1)
logging.info(food_itmes.burger2)
logging.info(food_itmes.biryani3)
logging.info(food_itmes.paneerpuff4)

