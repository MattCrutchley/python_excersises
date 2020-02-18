class students:
    __test = "hello"
    def __init__(self,age, name = "student"):
        self.age = age
        self.name = name
        


        

    def avgscore(self,score_1,score_2,score_3):
        return (score_1 + score_2 + score_3)/3

student1 = students(25,)
print(student1.avgscore(20,40,60))
print(getattr(student1,"name"))
student2 = students(25,"bill")
print(student2._students__test)
