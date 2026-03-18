# Author: Aaron Clure
# Email List Cleaner
# Create a program that will read a file and create a formatted copy of the file.

# open("file_name.file_type","x") : will create a file or return an error if the file exists
# open("file_name.file_type","w") : will create a file if the file does not exist
# open("file_name.file_type","a") : will create a file if the file does not exist
# with open(file, mode) as file :  will close the file when it is done
# 
# f = open("file_Name.fileType")
# print(f.read())                   will read and then print file content to the terminal

#!/usr/bin/env python3

import csv

output = "lab10_prospects_clean.csv"
input = open("D:\\PythonProgrammingLabs\\intro_programming_logic\\week13\\lab10_prospects.csv")

with open(output , "w") as file :
    writer = csv.writer(file)
    for row in input:
        writer.writerow(row)

print(f"New file created at {output}")
print(f"File created from {input}")