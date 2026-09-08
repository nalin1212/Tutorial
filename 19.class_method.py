class Empolyee:
    a=1

    @classmethod
    def show(cls):
        print(f"the class attribute of a {cls.a}")
e= Empolyee()
e.a =45

e.show()        
       