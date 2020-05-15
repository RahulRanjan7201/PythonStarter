myfile = open("routers.txt","r")
print(myfile.mode)
print(myfile.read())
print(myfile.read(5))
print(myfile.seek(0))
print(myfile.tell())
#Read first five character
print(myfile.read(5))
print(myfile.seek(0))
print(myfile.readlines())
print(myfile.seek(0))
for line in myfile.readlines() :
    if(line.startswith("A")) :
        print(line)
        
myfile = open("routers2.txt","x")