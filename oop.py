class Person:

    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone

    def generatecode(self):
        pass

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def display_data(self):
        return str("Name: "+self.getName()+" = address: "+self.getAddress()+" = phone: "+self.getPhone())

class Employee(Person):

   def __init__(self,name,address,phone,salary):
       super().__init__(name,address,phone)
       self.salary = salary

   def getSalary(self):
       return self.salary
   def display_data(self):
       return str(super().display_data()+" = Salary: "+str(self.getSalary()))
