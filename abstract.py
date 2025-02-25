from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(selpuri,first_name,last_name):
        selpuri.first_name=first_name
        selpuri.last_name=last_name

@property
def full_name(self):
    return f"{self.first_name}{self.last_name}"

@abstractmethod
def get_salary(self):
    pass

class FulltimeEmployee(Employee):
       def __init__(self,first_name,last_name,salary):
           super().__init__(first_name,last_name)
           self.salary= salary
         
       def get_salary(self):
            return self.salary
       
class hourlyEmoploye(Employee):
       def __init__(self,first_name,last_name,work_hour,rate):
           super().__init__(first_name,last_name)
           self.work_hour=work_hour
           self.rate=rate
       def get_salary(self):
            return self.work_hour*self.rate
     
e1=FulltimeEmployee("jhon","Doe",6000)
e2=hourlyEmoploye("jhon","Doe",6000)
print(e1)
