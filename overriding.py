class parent:
    def mymethod(self):
        print("calling parent method")

class child(parent):
    def mymethod(self):
       print("calling child method")

c=child()
c.mymethod()
        