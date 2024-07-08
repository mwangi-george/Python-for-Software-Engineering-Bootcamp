sample_dict = {"a": 1}

try:
    # Some code that might cause an exception (error)
    print(sample_dict["b"])
except Exception as e:
    print("We have encountered an error near", e)


try:
    print(sample_dict["b"])
except KeyError:
    print("We have encountered a key error")


# Chaining error handlers
try:
    print("This will work", sample_dict["a"])
    print("This will not work", sample_dict["b"])
except KeyError as k:
    print("We have encountered an error near", k)


try:
    2 / 0
except KeyError:
    print("We have encountered a key error")
except ZeroDivisionError as z:
    print("We have encountered a zero division error", z)


a = 1
b = 0
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    c = a / 1  # fall back value
    print(c)


# TODO: Raising exceptions

try:
    if b == 0:
        raise ZeroDivisionError
    c = a / b
except ZeroDivisionError:
    print("Hey there! Try not dividing by 0")
except NameError as n:
    print("Are you using an undefined variable")


# Custom Exceptions
class ThisIsOurCustomException(Exception):
    pass


try:
    if b == 0:
        raise ThisIsOurCustomException
    c = a / b
except ThisIsOurCustomException:
    print("We have encountered our custom exception")
finally:
    print("We have reached the finally block")
