# Data Abstraction
import logging
logging.basicConfig(filename ='test4-_-_-_-_-_DataAbstraction.log', level = logging.INFO, format ='%(levelname)s %(name)s %(asctime)s, %(message)s')


class ineuron:
    __students = 'DataScience'

    def students(self):
        logging.info('Print the class of student %s',ineuron.__students)


i = ineuron()
i.students()
i._ineuron__students
logging.info(i._ineuron__students)

