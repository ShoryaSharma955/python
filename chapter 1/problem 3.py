
#program to print the directory's content using os module
import os

# specify the directory you want to list
directory_path='/python old'

# list all the file and directory
contents=os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)
