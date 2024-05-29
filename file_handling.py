# creating a directory
import os
if not os.path.exists("files"):
    os.mkdir("files")
else:
    # opening a file in write mode (used when we know the file does not exist)
    # Overwrites content
    file_text = open("files/test_file.txt", "w")
    # Open in append mode (When the file already exist)
    file_csv = open("files/test_file.csv", "a")
    file_xls = open("files/test_file.xls", "w")
    file_tsv = open("files/test_file.tsv", "w")

    file_text.write("this is our first line\n")
    file_text.write("this is our second line")

    file_csv.write("name,age,George,23")

    # close connection to files
    file_text.close()
    file_csv.close()
    file_xls.close()
    file_tsv.close()
    print("Operation successful")
