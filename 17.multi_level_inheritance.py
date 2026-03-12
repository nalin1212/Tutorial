class Empolyee:
    a =1

class programmer(Empolyee):
    b=2

class manager(programmer):
    c=3

o = Empolyee()
print(o.a)  # Prints the attribute 
# print(o.b)
o = programmer ()
print (o.a,o.b)

o = manager()
print (o.a,o.b,o.c)