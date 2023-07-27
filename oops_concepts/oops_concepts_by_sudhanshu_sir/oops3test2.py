class bank :

    def transaction(self):
         print("total transaction value")


    def account_opening(self):
        print("this will show your your account open statues")


    def deposite(self):
        print("this will show your deposite account")


    def test(self):
        print("this is a test method form bank class")



class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icici throught hdfc")
    def test(self):
        print("this is a test method from hdfc bank")



class ineuron_bank:
    def account_satus_icici(self):
        print("print a account status in icici")


class icici(HDFC_bank, bank, ineuron_bank):
    pass

i = icici()
i.deposite()
i.transaction()
i.account_opening()
i.test()
i.account_satus_icici()












