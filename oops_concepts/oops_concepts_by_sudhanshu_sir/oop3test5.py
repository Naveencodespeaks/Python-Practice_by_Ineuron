class ineuron:
    def __init__(self):
        self.students1 = "student"


    def students(self):
        print(self.students1)


i = ineuron()
i.students()
i.students1 = "data Analytics"
i.students()




class ineuron1:
    def __init__(self):
        self.__students1 = "student"


    def students(self):
        print(self.__students1)

    def student_change(self, new_value):
        self.__students1= new_value

i1 = ineuron1()
i1.students()
i1.__students1 = "Big DATA"
i1.students()
i1.student_change("naveen")
i1.students()