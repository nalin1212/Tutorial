class empolyee:
    name="harry" 
    language = "py" # this is class attribute
    salary =120000
    
    def getinfo(self):
        print(f"The language is {self.language }.the salary is {self.salary }")

        

harry= empolyee()
# harry.greet()
harry.getinfo()
