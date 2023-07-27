# data abstraction
# where we are hiding the data behind some

class ineuron:
    __students = "datascience"


    def students(self):
        print("print the class of student", ineuron.__students)

i = ineuron()
i.students()
#i.__students # this will not work
print(i._ineuron__students)  # you have to go through class.


#print(i._ineuron__students)  # we have to go to class then to that variable
# so if we are going to hide the real implementation and user is trying to use it,
# so user is whom user is "i", "i" is an object, "i", is trying to use student variable.
# if some how if we are not giving a the direct access of an impimentation to user that is soming called as a "DATA_ABSTRACTION"


