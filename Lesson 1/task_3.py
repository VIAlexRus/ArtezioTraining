# Write a Python program to get a string made of the first 2
# and the last 2 chars from a given a string. If the string length
# is less than 2, return instead of the empty string. 


def first_and_last(str1):
    if len(str1) < 2:
        return ''
    return str1[0:2] + str1[-2:]


str1 = input('Enter string: ')

print(first_and_last(str1))
input('Press Enter to continue...')
