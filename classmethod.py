class student:
    def __init__(self,roll_no,name,age):
        self.roll_no = roll_no
        self.name= name
        self.age= age
    
    def show(self):
         print("Roll number:",self.roll_no,"name:",self.name,"Age:",self.age)

    def update(self,roll_number,age):
         self.roll_no=roll_number
         self.age=age
print('class VIII')
stud=student(20,"sugam","21")
stud.show()

print("haha")
stud.update(35,15)
stud.show()
    
    
      
       