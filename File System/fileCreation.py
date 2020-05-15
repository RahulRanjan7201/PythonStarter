newFile = open("newfile.txt","w")
newFile.write("I like Python!\n Do You?")
newFile.close();
newFile = open("newfile.txt","w")
newFile.write("This is great day today")
newFile.close()
newFile = open("newfile.txt","w")
newFile.writelines(("Cisco1","Juniper1", "HP1"))
# To write the data in end of file 
#for this case we need to A - for appending 
newFile.close();
newFile = open("newfile.txt","a")
newFile.write("hey geek we are writing")
newFile.close()

newFile = open("newfile.txt","w+")
newFile.write("come from w+ mode")
print(newFile.mode)
newFile.close()
