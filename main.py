text = "programming is amazing   "


print(text.index("z"))


print(text[0:10])

print(text.upper())

print(text.capitalize())

print(text.casefold())

print(text.center(2))
print(text.count("g"))

print(text.join("hhd"))

print(text.split("  ---   "))

print(text*3)

print(text.strip())

my_num = "2"

print(int(my_num))

x = 133 % 100
print(x)

# y = ""
# print(type(y))

# l_1 = [1, 23, 54]

# l_2 = ["a", "d"]

# print(l_1 + l_2)

# print(l_1.pop())

# tp = (1, 2, 3)
# tp[1] = 3
# print(tp)


my_dict = {
    "a": "A"
}

del my_dict["a"]
print(my_dict)


my_dict["nested_dict"] = {1: "a", 2: "b"}

print(my_dict)


# accessing values with get method
print(my_dict.get("nested_dict"))

# setting a default value
my_dict.setdefault("my_name", {1: 3, 4: 6})
print(my_dict)

# if the value alrady exists, setdefault has no effect
my_dict.setdefault("my_name", "GKM")
print(my_dict)


# ----------------Formatting strings
print(f"my dictionary is {my_dict}")

name = "Micah"
age = 23.34533
zip_code = 1234

# format age to 2 decimal places
# adding a defult number to zip code to make it 5 digits
print(f"name: {name}, age: {age:.2f}, Lives in {zip_code:05d}")

# TODO: Things are the things I should focus on

name = "Marcus"
age = 56

"""
The pass statement is used as a placeholder for future code. 
When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. 
Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
"""
if age <= 20:
    print(f"{age} is less than or equal to 20")
elif age <= 40:
    pass
elif age <= 60:
    pass
else:
    print(f"{age} is great than 60")


"""
The 'is' operator in Python is used to check if two variables point to the same object. 
Unlike the '==' operator, which checks if the values of two objects are equal, 
the 'is' operator goes one step further to ensure that they are, in fact, the exact same object.
"""
is_over_18 = age > 18

# using ==
if is_over_18 == True:
    print(f"{name} is over 18 years")

# using 'is' operator
if is_over_18 is True:
    print(f"{name} is over 18 years")

# using the variable itself
if is_over_18:
    print(f"{name} is over 18 years and getting old really fast")

random_none = None
if random_none is None:
    print("We have a none")

if age is not None:
    print("Age is not None")

age = 12
is_over_18 = age > 18
# negating
if not is_over_18:
    print("We are under 18")

"""
The default falsy value for numerical data types is 0
"""

random_value = 2
if random_value:  # truthy except for 0
    print(f"{random_value} is not zero")
else:
    print("This is zero")

"""
For tuples, lists, and dictionaries the default falsy value is when they are empty
"""

random_list = []
if random_list:
    print("The list is not empty")
else:
    print("The list is empty")


random_tuple = ()
if random_tuple:
    print("The tuple is not empty")
else:
    print("The tuple is empty")

random_dict = {}
if random_dict:
    print("The dictionary is not empty")
else:
    print("The dictionary is empty")
