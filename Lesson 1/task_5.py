# You are given with 3 sets, find if third set is a subset of the
# first and the second sets


def search_value(sets):
    set1 = set(sets[0])
    set2 = set(sets[1])
    set3 = set(sets[2])
    if set1 >= set3 and set2 >= set3:
        return 'True'
    else:
        return 'False'


str1 = input('Enter sets: ')
str1 = str1.replace('set([', '').replace(']', '').replace(')', '')
str1 = str1.replace(', ', ' ').split(' ')
sets = []
for key in str1:
    sets.append(key.split(','))

print(search_value(sets))
input('Press Enter to continue...')
