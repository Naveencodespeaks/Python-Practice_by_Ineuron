import logging
logging.basicConfig(filename = "force_gurkha.log", level = logging.INFO)
logging.info("This is the first logging example")
l = [1,2,3,4,5,6,7,8]
for i in l:
    if i ==2:
        logging.info(l)

# there are in genral 5 level of log
# 1. DEBUG  -----------> when ever we want to debug we have to use (logging.DEBUG)
# 2. warning ----------> what ever kind of warning information you want to show we can use (logging.warning)
# 3. error -------------> while running a code in between something have been occurred and we can write error message  like (logging.error)
# 4. critical------------>  when ever you got a seviour error at that point of time we can use(logging.critical)
# 5. INFO ----------------> what ever info you want to show we can use (logging.INFO)


# level of severity of each and every statement

# DEBUG    =  10
# INFO     =  20
# warning  =  30
# error    =  40
# critical =  50


logging.warning("This will try to load warning message with a tag warnin")
logging.warning("This is a warning for a user that they have found out 2 in the list")
logging.error("This is a error message from the system with a tag error")

# logging.shutdown() here after shutdown we cannot able to use the logging its terminate the process






