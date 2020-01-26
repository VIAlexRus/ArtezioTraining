# Write a Python program to count the number of characters
# (character frequency) in a string.


def number_char(x):
    dict = {}
    for char in x:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


x = input('Enter string, or press "Enter" to enter "google.com": ')
if len(x) == 0:
    x = 'google.com'

print(number_char(x))
input('Press Enter to continue...')
