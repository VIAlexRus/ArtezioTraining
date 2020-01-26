# You are asked to ensure that the first and last names of people begin with
# a capital letter in their passports.
# For example, alison heck should be capitalized correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.

import string


def caps():
    x = input('Enter surname: ')
    while (0 == len(x) or len(x) >= 1000):
        x = input('Enter the correct size of a name.',
                  ' It is no more than 1000 symbols and not empty: ')
    caps_str = string.capwords(x, sep=" ")
    return (caps_str)


print(caps())
input('Press Enter to continue...')
