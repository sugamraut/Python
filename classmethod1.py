class student1:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def calculate_age(cls,name,birth_year):
        return cls(name,date.today().year-birth_year)
    def show(self):
        print(self.name+"age is" + str(self.age))
    
jessa=student1("jessa",20)
jessa.show()

joy=student1.calculate_age("joy",1995)
joy.show()
        