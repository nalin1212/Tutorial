class person:
    def __init__(self, name, age, address=""):
        self.age = age
        self.name = name
        self.address = address

    def greet(self):
        print(f"my name is {self.name} and i am {self.age} years old")


person1 = person("Atul", 30)
person1.greet()
person2 = person("Alice", 30) 
person2.greet() 


        

        