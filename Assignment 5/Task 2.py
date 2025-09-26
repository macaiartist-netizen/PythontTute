# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

number = list(range(1,11))
extracted_list = number[0:5]
Reversed_list = extracted_list[::-1]
print('Original list:', number)
print('Extracted fisrt five elements:', extracted_list)
print('Reversed extracted elements:', Reversed_list)
