# opening a file
file_text = open("test_file.txt", "w")
file_csv = open("test_file.csv", "w")
file_xls = open("test_file.xls", "w")
file_tsv = open("test_file.tsv", "w")


file_text.write("this is our first line\n")
file_text.write("this is our second line")

file_csv.write("name,age,George,23")


# close connection to files
file_text.close()
file_csv.close()
file_xls.close()
file_tsv.close()
