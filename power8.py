num = int(input("Enter a number: "))

temp = num

while temp % 8 == 0 and temp > 1:
    temp = temp // 8

if temp == 1:
    print(num, "is a power of 8")
else:
    print(num, "is NOT a power of 8")