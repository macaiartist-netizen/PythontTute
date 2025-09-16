# Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

try:
    with open('Sample.txt', 'r') as file1:
        print('Reading file content:')
        num = 1
        for ummm in file1:
            print("Line",num,":", ummm, end='')
            num += 1
except FileNotFoundError:
    print("The file 'Sample.txt' was not found.")
