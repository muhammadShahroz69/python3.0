file_read = open("codingal.txt", "r")
print("Opened file in read mode")
print(file_read.read())
file_read.close()


# WRITE MODE
file_write = open("codingal.txt", "w")
print("Opened file in write mode")
file_write.write("Hello, I am a student and I am 12 years old\n")
file_write.close()


# APPEND MODE
file_append = open("codingal.txt", "a")
print("Opened file in append mode")
file_append.write("Hello, I am student2 and I like coding\n")
file_append.close()


# COUNT NUMBER OF LINES
file = open("codingal.txt", "r")
counter = 0
content = file.read()
line_list = content.split("\n")

for i in line_list:
    if i:
        counter += 1

print("Number of lines in file:", counter)
file.close()


# FILE MERGING PROJECT
firstfile = input("Enter the name of first file: ")
secondfile = input("Enter the name of second file: ")

f1 = open(firstfile, "r")
f2 = open(secondfile, "r")

print("\nContent of first file:")
print(f1.read())

print("\nContent of second file:")
print(f2.read())

f1.close()
f2.close()


# APPEND SECOND FILE INTO FIRST FILE
f1 = open(firstfile, "a")
f2 = open(secondfile, "r")

f1.write("\n" + f2.read())

f1.close()
f2.close()


# READ UPDATED FIRST FILE
f1 = open(firstfile, "r")
print("\nContent of first file after appending:")
print(f1.read())
f1.close()