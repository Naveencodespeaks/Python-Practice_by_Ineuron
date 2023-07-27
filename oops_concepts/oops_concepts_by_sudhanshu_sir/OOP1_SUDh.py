import logging
logging.basicConfig(filename="oops1_test_Bike_example.log", level = logging.INFO, format= '%(levelname)s,%(asctime)s, %(name)s %(message)s, ')
class bike:
    def __init__(two_wheeler, Brand_of_a_Bike, bike_name, Bike_model, Bike_variant):
        two_wheeler.brand = Brand_of_a_Bike
        two_wheeler.name = bike_name
        two_wheeler.model = Bike_model
        two_wheeler.variant = Bike_variant
# Here two_wheeler.brand, two_wheeler.name, two_wheeler.model, two_wheeler.variant are the class variables
# Where Brand_of_a_bike, bike_name, Bike_model, Bike_variant  "Alocations or referance or assignments operatiopn to a class variables"

logging.info("Here brand, name, model, variant are the class variables")

Royal_enfield = bike("Royal Enfield", "Classic", "350CC", "topend")
logging.info("Bike Name: " + Royal_enfield.brand)
logging.info(Royal_enfield.name)
logging.info(Royal_enfield.model)
logging.info(Royal_enfield.variant)





