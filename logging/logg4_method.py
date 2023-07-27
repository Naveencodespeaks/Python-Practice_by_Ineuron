import logging
logging.basicConfig(filename = "force_gurkha4.log",level = logging.INFO, format = '%(levelname)s %(asctime)s %(name)s  %(message)s')

try:
    logging.info("I am trying to read a file")
    with open("Royal Enfield_Himalaya.txt", 'r'):
        logging.info("succsfully it had read the file")

except Exception as e:
    logging.info("This is a situation for us")
    logging.error(e)
    logging.exception(e)
