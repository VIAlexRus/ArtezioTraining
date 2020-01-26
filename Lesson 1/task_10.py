# Write a Python program to get the difference between the two lists


def diff(list1, list2):
    return (list(set(list1) - set(list2)))


list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

print(diff(list1, list2))
