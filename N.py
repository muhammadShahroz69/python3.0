# Multiply using 1 iteration (direct multiplication)
def multiply_one_iteration(n, m):
    return n * m


# Multiply using N iterations (repeated addition)
def multiply_n_iterations(n, m):
    result = 0
    for i in range(n):
        result += m
    return result


# Taking input
n = int(input("Enter value of N: "))
m = int(input("Enter value of M: "))

print("Using 1 iteration:", multiply_one_iteration(n, m))
print("Using N iterations:", multiply_n_iterations(n, m))