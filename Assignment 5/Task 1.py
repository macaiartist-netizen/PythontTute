# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

dict = {
        'Arun':55,
        'Ankit':75,
        'Anjana':95
        }
name = input('Enter the student\'s name: ')
if name in dict:
    print('{}\'s marks: {}'.format(name,dict[name]))
else:
    print('student not found.')