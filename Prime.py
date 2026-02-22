print("Two Digit Prime Numbers are:")

for num in range(10, 100):   # Loop from 10 to 99
    is_prime = True

    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        print(num)