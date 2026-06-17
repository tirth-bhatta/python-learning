# Import the os module to work with operating system functions
import os

# Specify the directory path ('.' means the current directory)
path = "."

# Get a list of all files and folders in the directory
contents = os.listdir(path)

# Print each item found in the directory
for item in contents:
    print(item)