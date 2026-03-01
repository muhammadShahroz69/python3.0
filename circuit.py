# Taking inputs (0 or 1)
A = int(input())
B = int(input())
C = int(input())

# Applying bit operations
output = (A & B) | (~C & 1)

print(output)