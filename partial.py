from functools import partial

def multiply(a, b):
    return a * b

# Fix the first argument as 10
multiply_by_10 = partial(multiply, 10)

print(multiply_by_10(5))
print(multiply_by_10(8))
