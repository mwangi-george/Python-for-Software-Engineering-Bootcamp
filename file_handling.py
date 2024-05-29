# # creating a directory
# import os
# if not os.path.exists("files"):
#     os.mkdir("files")
# else:
#     # opening a file in write mode (used when we know the file does not exist)
#     # Overwrites content
#     file_text = open("files/test_file.txt", "w")
#     file_text.write("this is our first line \n")
#     file_text.close()

#     # Open in append mode (When the file already exist)
#     file_text = open("files/test_file.txt", "a")
#     file_text.write("this is our second line (file handling)\n")
#     file_text.write("this is our third line (file handling)\n")
#     file_text.write("this is our fourth line (file handling)\n")
#     file_text.write("this is our fifth line (file handling)\n")
#     file_text.close()

#     file_csv = open("files/test_file.csv", "w")
#     file_csv.write("name,age,George,23")
#     file_csv.close()

#     # open file in read mode
#     file_text = open("files/test_file.txt", "r")
#     file_content = file_text.read()
#     print(file_content)

#     file_line = file_text.readline()
#     print(file_line)

#     for line in file_text.readlines():
#         print(line)

#     file_text.close()

# print("Operation successful")

# Using context manager (we dont have to close file)
with open("files/test_file.txt", "r") as f:
    content = f.read()
    print(content)

    for line in f.readlines():
        print(line)

    