# multilevel inheritance
import logging
logging.basicConfig(filename ='test2_bank----multilevel-inheritance.log', level = logging.INFO, format ='%(levelname)s %(name)s %(asctime)s, %(message)s')


class bank:
    def transaction(self):
        logging.info('Total  transaction value')

    def account_opening(self):
        logging.info("This will showing  you  your account open status")
    def deposits(self):
        logging.info('This will show your deposited amount')


class HDFC_bank(bank):

    def hdfc_to_icici(self):
        logging.info('This will show you all the transaction happend to icici throught hdfc')

class icici(HDFC_bank):
    pass


i = icici()
logging.info(i)
i.hdfc_to_icici()  # here we can use logging.info to log the out but if we do so, the it will give me the values and "none" value too
i.transaction()
logging.info(i.account_opening()) # here we can see that we can able to log the value and "none" value too!!!!
logging.info(i.deposits())         # so that is the different between logging.info(function()) and normal function()

