# Write a Python program to count the number of strings
# where the string length is 2 or more
# and the first and last character are same from a given list of strings. 


def quantity_string(srt1):
    quantity = 0
    for x in str1:
        if len(x) >= 2 and x[0] == x[-1]:
            quantity += 1
    return quantity


str1 = input('Enter the string list, or press "Enter"',
             ' to enter default string: ')
if len(str1) == 0:
    str1 = ['abc', 'xyz', 'aba', '1221']
else:
    str1 = str1.split(' ')

print(quantity_string(str1))
input('Press Enter to continue...')
