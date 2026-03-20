# Author: Aaron Clure
# Email List Cleaner
# Create a program that will read a file and create a formatted copy of the file.

# open("file_name.file_type","x") : will create a file or return an error if the file exists
# open("file_name.file_type","w") : will create a file if the file does not exist (will overwrite)
# open("file_name.file_type","a") : will create a file if the file does not exist (add changes)
# with open(file, mode) as file :  will close the file when it is done
# newline = "" will prevent double spacing
# 
# f = open("file_Name.fileType")
# print(f.read())                   will read and then print file content to the terminal

#!/usr/bin/env python3
import csv
input_path = r"intro_programming_logic\week13\lab10_prospects.csv"
output_path = r"intro_programming_logic\week13\lab10_prospects_clean.csv"

with (open(input_path, mode="r") as infile,
  open(output_path, mode="w", newline="") as outfile):
    
  reader = csv.reader(infile)
  writer = csv.writer(outfile)
    
  for row in reader:  
    first_name = row[0].strip().title()
    last_name  = row[1].strip().title()
    email      = row[2].strip().lower()
    writer.writerow([first_name, last_name, email])


print(f"\n\n")
print(f"Welcome to the Email List Cleaner\n")
print(f"Source list:  lab10_prospects.csv")
print(f"Cleaned list: lab10_prospects_clean.csv ")
print(f"\nCongratulations! Your list has been cleaned!")
print(f"\n\n")
