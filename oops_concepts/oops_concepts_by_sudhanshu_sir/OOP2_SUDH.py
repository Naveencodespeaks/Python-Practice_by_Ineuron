import logging
logging.basicConfig(filename ='oops2_test1.log', level = logging.INFO, format ='%(levelname)s %(asctime)s %(name)s %(message)s')

class ineuron():
    def __init__(self, employe_name, employe_mailid, employe_gender, employe_phone_no, employe_role, employe_salary):
        self.employe_name = employe_name
        self.employe_mail_id = employe_mailid
        self.employe_gender = employe_gender
        self.employe_phone_no = employe_phone_no
        self.employe_role = employe_role
        self.employe_salary = employe_salary

madava_var = ineuron("Madhava", 'Madhava@gmail.com', 'male', 1234567898, 'Full stack data science', 250000)
logging.info(madava_var.employe_name)
logging.info(madava_var.employe_gender)
logging.info(madava_var.employe_role)
logging.info(madava_var.employe_mail_id)
logging.info(madava_var. employe_phone_no)
logging.info(madava_var.employe_salary)


class person():
    def age(self, current_year, year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, email_id):
        logging.info("take and mail id from a person and print it " + email_id)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("Tell me your date of birth")
        return dob


sudh = person()
anuj = person()
gargi = person()
krish = person()
hitesh = person()
sudh.email_id_input("sudhanshu@ineuron.ai")
sudh.ask_name()
hitesh.ask_dob()


