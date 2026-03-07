n = int(input("Enter a number: "))
position = 1

while n > 0:
    if n & 1:
        print(position)
        break
    n = n >> 1
    position += 1