# TODO:--- functions
def add_one(number: int):
    number += 1
    return number


print(add_one(3))


def add_subtract_numbers(num_1: int, num_2: int):
    return num_1 + num_2, num_1 - num_2


print(add_subtract_numbers(34, 23))

added, subtracted = add_subtract_numbers(20, 34)
print(added, subtracted)
print(type(added), type(subtracted))


def add_subtract_multiply_divide_numbers(num_1: int, num_2: int):
    return num_1 + num_2, num_1 - num_2, num_1 * num_2, num_1 / num_2


print("Started discarding")

# get the first return and discard the rest
added, *_ = add_subtract_multiply_divide_numbers(23, 43)
print(added)

# get the last return and discard the rest
*_, val = add_subtract_multiply_divide_numbers(23, 43)
print(val)

# get the fast and last return and discard the middle values
added, *_, divided = add_subtract_multiply_divide_numbers(23, 43)
print(added, divided)
