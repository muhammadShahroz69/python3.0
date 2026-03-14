num = int(input("Enter a number: "))

binary = bin(num)[2:]
reverse_binary = binary[::-1]

result = int(reverse_binary, 2)

print("Binary:", binary)
print("Reversed Binary:", reverse_binary)
print("Result:", result)