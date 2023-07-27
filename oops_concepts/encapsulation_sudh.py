import logging
logging.basicConfig(filename ='encapsulation_test4.log', level = logging.INFO, format ='%(levelname)s %(name)s %(asctime)s, %(message)s')

class ineuron:
    def __init__(self):
        self.student1 = 'data science'

    def students(self):
        logging.info(self.student1)

i = ineuron()
i.students()
i.student1 = 'data analytics'
i.students()


class ineuron1:
    def __init__(self):
        self.__student1 = 'data science'

    def students(self):
        logging.info(self.__student1)

    def student_change(self, new_value1):
        self.__student1 = new_value1

i = ineuron()
i1 = ineuron1()
i.students()
i.student1 = 'data analytics'
i.students()
i1.students()
i1.__student1 = 'Bigdata'
i1.students()
i1.student_change("Hare krishna")
i1.students()