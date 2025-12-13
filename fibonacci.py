# Fibonacci Series Project

def fibonacci(n):
    a = 0
    b = 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


# main program
print("=== Fibonacci Series Project ===")

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    fibonacci(n)