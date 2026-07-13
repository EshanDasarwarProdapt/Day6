from functools import cmp_to_key

def compare(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0

numbers = [5, 2, 8, 1, 4]

sorted_numbers = sorted(numbers, key=cmp_to_key(compare))

print(sorted_numbers)
