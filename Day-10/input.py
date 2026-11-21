# number = input("please Provide a number:")
# print(number)
import os
folders = input("Enter a list of folders names with separated by spaces: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Folder not found: " + folder)
        break
    except PermissionError:
        print("Permission denied: " + folder)
        break
    

    print( " === listing files for the folder - " + folder)

    for file in files:
        print(file)
