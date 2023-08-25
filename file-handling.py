import os

print(os.getcwd())  # current working directory
myFile = open("text.txt", "w+")
print(myFile)  # object's data

# reading the file:
reader = myFile.read()
print(reader)

myFile.seek(0)  # to make the pointer start from the begging

# writing in the file :
line1 = "writing..."
myFile.write(line1)
print(myFile.read())

myFile.seek(0)
# counting lines in the file :
count = 0
for line in myFile:
    count = count + 1
print("lines num = ", count)

myFile.seek(0)

# searching in the file : (using startswith())
for line in myFile:
    # The rstrip() method removes any trailingcharacters (characters at the end a string), space is the default trailingcharacter to remove.
    line = line.rstrip()  # removing the additional spaces at the end of the string
    if line.startswith("s"):
        print(line)

myFile.seek(0)

# another way
for line in myFile:
    line = line.rstrip()
    if not line.startswith("s"):
        continue
    print(line)

myFile.seek(0)
# another way : (using find())
for line in myFile:
    line = line.rstrip()
    if line.find("x") == -1:
        continue
    print(line)

myFile.seek(0)
# Letting the user choose the file name:
filename = input("plz enter file name ")
try:
    my2file = open(filename, "w")
except:
    print(f"{filename} is not found")
    exit()
# code if the filename is correct:
