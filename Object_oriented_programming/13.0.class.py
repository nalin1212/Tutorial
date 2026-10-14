# object oriented programming is a programming paradigm that uses objects and classes to organize code. 
#inside a class, we can define attributes (variables) and methods (functions) that belong to the class.
# It allows for encapsulation, inheritance, and polymorphism, which can make code more modular, reusable, and easier to maintain.
class Dog: #class is a blueprint for creating objects. It defines the properties and behaviors that the objects will have.
    def __init__(self,name,breed,owner):
        self.name =name 
        self.breed = breed
        self.owner =owner #attributes are variables that belong to the class and can be accessed using the self keyword.
        pass
    def bark(self): #methods are functions that belong to the class and can be called using the self keyword.
         print ('bhau bhau')
class owner:
    def __init__(self,name ,address, contact_number) :
        self.name =name 
        self.address =address  
        self.phone_number = contact_number
owner1=owner("Danny","122 springfield Drive","568689")
dog1= Dog("Bruce","papillion",owner1)
dog1.bark()
print(dog1.owner.name)
print(dog1.name)