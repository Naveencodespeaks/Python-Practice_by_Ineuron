# Method over riding
import logging
logging.basicConfig(filename ='test3_method-OverRiding.log', level = logging.INFO, format ='%(levelname)s %(name)s %(asctime)s, %(message)s')


class ineuron:
    def student(self):
        logging.info('print the details of all the studnts')
    def achivers(self):
        logging.info('print  the list of all achiver')
    def hall_of_fame(self):
        logging.info('print everyone form hall of fame')

class ineuron_vision(ineuron):

    def student(self):
        logging.info('These are the filtered student list')   # This is  method overriding
    def achivers(self):
        logging.info('these are filtered achivers list')


iv =ineuron_vision()
iv.student()
iv.achivers()
iv.hall_of_fame()

