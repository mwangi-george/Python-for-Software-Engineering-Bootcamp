# text = "programming is amazing   "


# print(text.index("z"))


# print(text[0:10])

# print(text.upper())

# print(text.capitalize())

# print(text.casefold())

# print(text.center(2))
# print(text.count("g"))

# print(text.join("hhd"))

# print(text.split("  ---   "))

# print(text*3)

# print(text.strip())

# my_num = "2"

# print(int(my_num))

# x = 133 % 100
# print(x)

# # y = ""
# # print(type(y))

# # l_1 = [1, 23, 54]

# # l_2 = ["a", "d"]

# # print(l_1 + l_2)

# # print(l_1.pop())

# # tp = (1, 2, 3)
# # tp[1] = 3
# # print(tp)


# my_dict = {
#     "a": "A"
# }

# del my_dict["a"]
# print(my_dict)


# my_dict["nested_dict"] = {1: "a", 2: "b"}

# print(my_dict)


# # accessing values with get method
# print(my_dict.get("nested_dict"))

# # setting a default value
# my_dict.setdefault("my_name", {1: 3, 4: 6})
# print(my_dict)

# # if the value alrady exists, setdefault has no effect
# my_dict.setdefault("my_name", "GKM")
# print(my_dict)


# # ----------------Formatting strings
# print(f"my dictionary is {my_dict}")

# name = "Micah"
# age = 23.34533
# zip_code = 1234

# # format age to 2 decimal places
# # adding a defult number to zip code to make it 5 digits
# print(f"name: {name}, age: {age:.2f}, Lives in {zip_code:05d}")

# # TODO: Things are the things I should focus on

# name = "Marcus"
# age = 56

# """
# The pass statement is used as a placeholder for future code.
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
# """
# if age <= 20:
#     print(f"{age} is less than or equal to 20")
# elif age <= 40:
#     pass
# elif age <= 60:
#     pass
# else:
#     print(f"{age} is great than 60")


# """
# The 'is' operator in Python is used to check if two variables point to the same object.
# Unlike the '==' operator, which checks if the values of two objects are equal,
# the 'is' operator goes one step further to ensure that they are, in fact, the exact same object.
# """
# is_over_18 = age > 18

# # using ==
# if is_over_18 == True:
#     print(f"{name} is over 18 years")

# # using 'is' operator
# if is_over_18 is True:
#     print(f"{name} is over 18 years")

# # using the variable itself
# if is_over_18:
#     print(f"{name} is over 18 years and getting old really fast")

# random_none = None
# if random_none is None:
#     print("We have a none")

# if age is not None:
#     print("Age is not None")

# age = 12
# is_over_18 = age > 18
# # negating
# if not is_over_18:
#     print("We are under 18")

# """
# The default falsy value for numerical data types is 0
# """

# random_value = 2
# if random_value:  # truthy except for 0
#     print(f"{random_value} is not zero")
# else:
#     print("This is zero")

# """
# For tuples, lists, and dictionaries the default falsy value is when they are empty (their length is 0)
# """

# random_list = []
# if random_list:
#     print("The list is not empty")
# else:
#     print("The list is empty")


# random_tuple = ()
# if random_tuple:
#     print("The tuple is not empty")
# else:
#     print("The tuple is empty")

# random_dict = {}
# if random_dict:
#     print("The dictionary is not empty")
# else:
#     print("The dictionary is empty")


# # TODO:--- For Loops

# for i in range(0, 4):
#     print("Hello")
#     print(i)

# random_list = ["a", "b", "c", "d", "e"]
# for index in range(len(random_list)):
#     value = random_list[index]
#     print(index, value)


# print("List is now")
# print(random_list[index])

# second_list = ["x", "y", "z"]


# print("")
# for value in random_list:
#     print(value)
#     for second_value in second_list:
#         print(second_value)
#         total_value = value + second_value
#         print(total_value)

# # placeholder variables in the for loop
# for _ in range(5):  # _ is a placeholder since we are not using it anywhere inside the loop
#     print("Hi")


# # When two or more objects are connected we can use the zip method to iterate over them simultaneoulsy
# names = ["George", "Kevin", "Michael"]
# ages = [25, 23, 45]
# heights_cm = [156, 190, 201]

# # Iterate over the 3 objects
# for name, age, height in zip(names, ages, heights_cm):
#     print(name, age, height)
#     print(f"{name} is {age} years old and {height}cm tall")


# # TODO:--- While loops
# # Means while a certain condition is TRUE
# my_age = 24

# while my_age > 25:
#     print(f"{my_age} is greater than 25")
# else:
#     print(f"{my_age} is less than 25")


# count = 0
# while count < 10:
#     print(count)
#     count += 1

# invest_amt = 50_000
# target = 500_000

# while invest_amt < target:
#     invest_amt += 50_000
#     print(f"Continue investing, you are now at {invest_amt}")


# count = 0
# while True:
#     count += 1
#     if count % 2 == 0:  # checking if even
#         continue  # skip even numbers and restart the loop at the next odd nummber
#     print(count)

#     # break the loop until when count is greater than 20
#     if count >= 20:
#         break

# # continue in for loop
# for i in range(20):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# print("while loop started")
# x = 0
# while x < 4:
#     x += 1
#     print(x)
#     break  # break from the loop after adding 1


# invest_amt = 50_000
# while invest_amt <= 500_000:
#     invest_amt += 50_000

#     if invest_amt > 500_000:
#         break
#     print(invest_amt)


# val = 1
# while val <= 20:
#     print(val)
#     val += 2
# else:
#     print(f"{val} is no longer less than or equal to 20")

# val = 1
# while val <= 20:
#     print(val)
#     val += 3
# else:
#     print(f"{val} is now greater than 20")


# if item is banana, skip to the next
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)


# def print_if_odd(number):
#     if number % 2 == 0:
#         return  # similar to break
#     print(number)


# count = 0
# while True:
#     count += 1
#     print_if_odd(number=count)
#     if count >= 20:
#         break


# for i in range(20):
#     print_if_odd(i)

# age = 0
# while True:
#     age += 1
#     if age >= 24:
#         break
#     print(age)


def add_numbers(number_1: int, number_2: int):
    return number_1 + number_2, number_1 - number_2, number_1 * number_2


added_num, subtracted_num, multiplied_num = add_numbers(2, 4)
print(subtracted_num, multiplied_num)

# assign the first value and discard the rest
added_num, *_ = add_numbers(3, 5)
print(added_num)


# Write a program that prints out a left oriented triangle of x’s with a height of 5. Your final result
# should look like this.
# x
# xx
# xxx
# xxxx
# Xxxxx

# def print_triangle(height):
#     for i in range(1, height + 1):
#         print('x' * i)


# print_triangle(5)
def print_centered_triangle(height):
    for i in range(1, height + 1):
        # Calculate the number of 'x's for the current row
        num_xs = 2 * i - 1
        # Calculate the number of spaces needed for centering
        num_spaces = height - i
        # Print the centered row
        print(' ' * num_spaces + 'x' * num_xs)


print_centered_triangle(5)


"""using dictionary to provide input values"""

# define function


def calculator(num1: int, num2: int):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2


# store arguments in a dictionary, (keys must match function parameters)
my_numbers = {"num1": 3, "num2": 2}

# use double asteric to unpack the dictionary
print(calculator(**my_numbers))


# unpacking a list
first = 2
second = 3

my_numbers = [first, second]
print(my_numbers)

# use single asteric to unpack a list when passing arguments
print(calculator(*my_numbers))


# unamed parameters in function definition
def calculator(num1: int, num2: int, *args):
    print(args)  # positional arguments
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2


print(calculator(10, 5, 3, 4, 100, 200))


# passing unknown keyword arguments
def calculator(num1: int, num2: int, *args, **kwargs):
    print(args)  # positional arguments
    print(kwargs)  # returns a dictionary
    print("Mike's Age: ", kwargs.get("mike"))
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2, args, kwargs


print(calculator(10, 5, 30, 45, me=20, mike=10, moses="hello world"))


def second(test_1, test_2):
    print(test_1, test_2)


def calculator(num_1, num_2, *args, **kwargs):
    print(kwargs)
    second(**kwargs)  # unpack additional keyword arguments


print(calculator(2, 2, test_1=4, test_2=5))


"""Global & Local Variables"""
height_cm = 180  # this is a global variable (has larger scope)


def name():
    name = "George"  # this is a local variable
    print(name)


def height_m(x: float):
    global height_cm  # access & manipulate global variables
    height_cm = x
    height_metres = height_cm / 100
    return height_metres


print("****************Global Variables**************")
print(height_m(140))
print(height_cm)
