# Least Common Multiple Project

# Function to find GCD using Euclidean Algorithm
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find LCM
def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculating LCM
result = find_lcm(num1, num2)

print("The LCM of", num1, "and", num2, "is:", result)