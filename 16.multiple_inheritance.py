class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class Coder:
    language = "Python"

    def printlanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def Showlanguages(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee("Rahul", 50000)
b = Programmer("Aman", 80000)

b.show()
b.printlanguages()
b.Showlanguages()