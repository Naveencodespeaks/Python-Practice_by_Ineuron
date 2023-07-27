from utils.utill1 import person2

obj = person2("hare","krishna", 1234)
print(obj.yob1)
print(obj._name123)
print(obj.yob1)
print(obj._person2__surname321)


class person1:
    def __init__(self, name, surname, yob):            # _ means it is protected
        self._name123 = name                           # __ means it is private
        self.__surname321 = surname                     # no underscore it is public
        self.yob1 = yob

naveen = person1("naveen", "Adep", 1996)
print(naveen._person1__surname321)                      # object._classname__variable
print(naveen.yob1)                                      # naveen._person__surname321
print(naveen._name123)


# packages and modules are nothing but just like a folder and file
# where package is called as folder in general word's
# where modules are files in the folder, and we can use any modules like class, function,...etc my importing packages
# we can also perform the import folder files into another files like from folder name.filename import class or function...etc
# EXAMPLE for importing file from another folder is this oops_day2.py code

# syntax is like from utils.utill1 mport person2

