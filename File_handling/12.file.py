''''
a="a very long string emails"
emails =[]
3 seconds 
'''
'''f=open("dict.txt","w")
data= f.read()
print (data)
f.close()
'''
line = open("dict.txt", "r")
data =line.readline()
while (data != ""):
    print (data)
    data=line.readline()

line.close()    
