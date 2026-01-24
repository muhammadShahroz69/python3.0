file =open('condingal.txt', 'r')
print(file.read())
file.close()
file =open('condingal.txt', 'r')
print("/n read in parts /n")
print(file.read(5))
print(file.read(7))
file.close()


file = open('condingal.txt','w')
file.write("hi i am Obito and i am 18 years old")
file.close()

file = open('condingal.txt','a')
file.write("hi i am Obito and i am 18 years old")
file.close()

with open('condingal.txt','r') as file1:
  with open('condingal2.txt','w') as file2:
    for line in file1:
        if not(line.startswith('condinagl')):
            print(line, end='')

file = open ('condingal.txt','r')
file2=open ('condingal2.txt','w')  
cont = file.readline()
type(cont)
for i in range(1,len(cont)+1):
    if i %2!=0:
        file2.write(cont[i-1])
    else:
        pass
file.close()

fn1= open('condingal2.txt','r')
cont1=fn1.read()
print(cont1)
fn1.close()
file2.close()