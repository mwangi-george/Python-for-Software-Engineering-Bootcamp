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
