# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.


a = int(input('Enter a number:'))

if a%2 == 0:
    print(str(a)+' is an even number')
else:
    print(str(a)+' is an odd number')

# using f-string, cleaner and recommended:
# if a % 2 == 0:
#     print(f"{a} is an even number")
# else:
#     print(f"{a} is an odd number")