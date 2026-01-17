file_read= open('condingal.txt','r')
print("open file in read mode")
print(file_read.read())
file_read.close()

file_write=open('condingal.txt','w')
print("open file in write mode")
file_write.write("hello i am student and i am 12 years old")
file_write.close()


file_append=open('condingal.txt','a')
print("open file in appent mode")
file_append.write("hello i am student2 and i like coding")
file_append.close()

file=open('condingal.txt','r')
counter = 0
content = file.read()
colist = content.split("/n")
for i in colist:
    if i:
      counter+=1
print("this is the number of lines in file")
print(counter)  



firstfile=input("Enter the name of first file:")
secondfile=input("Enter the name of second file:")
f1=open(firstfile,'r')
f2=open(secondfile,'r')
print("the content in first file is:")
print(f1.read())
print("the content in second file is:")
print(f2.read())
f1.close()
f2.close()
f1=open(firstfile,'a+')
f2=open(secondfile,'r')
f1.write(f2.read())
f1.seek(0)
f2.seek(2)
print("content in first file after appending:")
print(f1.read())
print("content in second file after appending:")
print(f2.read())
f1.close()
f2.close()