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
