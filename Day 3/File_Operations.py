#Read from File
file=open("f1.txt","r")
content=file.readline()
content1=file.readlines()
print(content)
print(content1)
file.close()

#Append to file
file=open("f1.txt","a")
file.write("\n New Line Added")
file.close()

#Write to File
file=open("f1.txt","w")
file.write("Hello Python\n")
file.write("This is my write example")
file.close()