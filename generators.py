import os


def populate_file(filename):
    values_to_write = ["line 1", "Line 2", "Line 3"]
    with open(filename, "w") as out:
        for value_to_write in values_to_write:
            out.write(value_to_write)
            out.write("\n")


filename = "sample_file.txt"
populate_file(filename)


# def read_file(filename):
#     data = []
#     with open(filename, "r") as in_file:
#         for line in in_file:
#             data.append(line)

#     return data


# data = read_file("sample_file.txt")
# print(data)


# using generators

def read_file(filename):
    with open(filename, "r") as in_file:
        for line in in_file:
            yield line


file_contents = read_file(filename)
print(file_contents)  # <generator object read_file at 0x000001BF5D974F40>

for line in file_contents:
    print(line)


# short cut (Generator expression)
file_contents = (line for line in open(filename, "r"))
print(file_contents)


def read_if_exists(filename):
    if os.path.isfile(filename):
        return True
    return False


print(read_if_exists(filename))


def read_if_exists(filename):
    if os.path.isfile(filename):
        yield from read_file(filename)
    return []


file_contents = read_if_exists(filename)
print(file_contents)  # <generator object read_if_exists at 0x0000021BDA824B80>

for line in file_contents:
    print(line)
