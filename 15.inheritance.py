class Employee:
    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee("Rahul", 50000)
b = Programmer("Aman", 80000, "Python")

print(a.company, b.company)

a.show()
b.showlanguage()