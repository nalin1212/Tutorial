class empolyee:
    name="harry" 
    language = "py" # this is class attribute
    salary =120000
    def _init_(self,name ,salary,language):#dunder  method which is automatically called
        self.name =name 
        self.salary =salary 
        self.language =language
        print("I am creating  an object")
    
    def getinfo(self):
        print(f"The language is {self.language }.the salary is {self.salary }")
    @staticmethod
    def greet():
        print ("good morning ")            

        

harry= empolyee()
# harry.greet()
harry.getinfo()
