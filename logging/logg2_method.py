import logging
logging.basicConfig(filename = 'force_gurkha2.log', level = logging.DEBUG, format = '%(levelname)s %(name)s %(asctime)s  %(message)s')



# level of severity of each and every statement

# DEBUG    =  10
# INFO     =  20
# warning  =  30
# error    =  40
# critical =  50

def devide(a,b):
    logging.info("This number entered by user is %s and %s", a,b)
    try:
        logging.info("We are into function")
        div = a/b
        logging.info("we have completed a division operation")
        logging.info("result of code is  %s",  div)
        return div
    except Exception as e:
        logging.exception(e)
(devide(3,7))

