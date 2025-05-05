class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        print(f" Full Name is {self.fname} {self.lname}")

person1 = person('vishnu','vardhan')
person1.fullName()