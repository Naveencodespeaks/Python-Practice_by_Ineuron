# multiple_ inheritance
import logging
logging.basicConfig(filename ='test2_bank----multiple-inheritance.log', level = logging.INFO, format ='%(levelname)s %(name)s %(asctime)s, %(message)s')


class bank:
    def transaction(self):
        logging.info('Total  transaction value')

    def account_opening(self):
        logging.info("This will showing  you  your account open status")
    def deposits(self):
        logging.info('This will show your deposited amount')

    def test(self):
        logging.info('This is a test method from bank class')


class HDFC_bank:

    def hdfc_to_icici(self):
        logging.info('This will show you all the transaction happend to icici throught hdfc')
    def test(self):
        logging.info('This is a test from HDFC Bank')

class ineuron_bank:
    def account_status_icici(self):
        logging.info('This message is coming from ineuron_bank class: Print a account ststus in icici ')

class icici(HDFC_bank, bank,ineuron_bank): # This is known as multiple-inheritance
    pass

i = icici()
i.hdfc_to_icici()
i.transaction()
i.account_opening()
i.deposits()
i.test() # if we have a same function or same name conflict, at that point of time test() is going to take first function class in that icici() this give you the output from HDFC_Bank class
i.account_status_icici()



