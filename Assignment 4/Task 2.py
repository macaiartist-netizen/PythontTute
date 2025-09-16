# Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

text1 = input('Enter text to write to the file: ')
with open('output.txt', 'w') as file1:
    file1.write(text1+'\n')
print('Data successfully written to output.txt.')

text2 = input('\nEnter additional text to append: ')
with open('output.txt', 'a') as file2:
    file2.write(text2)
print('Data successfully appended.')

print('\nFinal content of output.txt: ')
with open("output.txt", "r") as file3:
    for neww in file3:
        print(neww,end='')