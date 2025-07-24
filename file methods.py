file = open("sample.txt","r")
#read the entire file
content = file.read()
print(content)
#reading every line and storing in a list
content1 = file.readlines()
print(content1)
#read each line
content2 = file.readline()
print(content2)
content2 = file.readline()
print(content2)
content2 = file.readline()
print(content2)

file.close()

file = open("sample1.txt","w")
file.write("I made a new file")
#add a new line next to the previous one
file = open("sample1.txt","a")
file.write("\nI made a new new file")