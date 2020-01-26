# Написать программу, которая принимает от пользователя имя и пароль.
# Сравнивает пароль с заданным в коде.

user_base = {'test': 'test', 'admin': 'admin',
             'Иван': '123', 'Павел': 'qwe',
             'Дарья': 'qaz'}

while True:
    login = input('Login: ')
    password = input('Password: ')
    if login in user_base and password == user_base[login]:
        print('Password for user:', login, 'is correct')
        break
    else:
        print('Password for user:', login,
              'is incorrect \nPlease try again...')
