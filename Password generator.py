# Генератор безопасных паролей

# проверка введенного значения для количества и длины паролей
def is_valid(s) :
    return s.isdigit() and int(s) > 0

def generating_password(num, s) :
    password = ''
    for j in range(num) :
        password += choice(s)
    return password

from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception = 'il1Lo0O'
chars = '' # набор символов для генерации паролей

print('Добро пожаловать в генератор паролей!')

flag = 11 # метка необходимости повторного ввода количества и / или длины паролей

while flag == 11 :
    pass_quantity = input('Какое количество паролей необходимо сгенерировать? ')
    if is_valid(pass_quantity) == False :
        print('Необходимо именно целое число больше 0')
    else :
        pass_quantity = int(pass_quantity)
        flag = 10

while flag == 10 :
    pass_lenght = input('Какой должна быть длина пароля? ')
    if is_valid(pass_lenght) == False :
        print('Необходимо именно целое число больше 0')
    else :
        pass_lenght = int(pass_lenght)
        flag = 0

digits_on = input('Использовать ли цифры 0123456789? (д = да, иной символ = нет): ')
lowercase_on = input('Использовать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д = да, иной символ = нет): ')
uppercase_on = input('Использовать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д = да, иной символ = нет): ')
punctuation_on = input('Использовать ли символы !#$%&*+-=?@^_? (д = да, иной символ = нет): ')
exception_on = input('Исключить неоднозначные символы il1Lo0O? (д = да, иной символ = нет): ')

if digits_on.lower() == 'д' :
    chars += digits

if lowercase_on.lower() == 'д' :
    chars += lowercase_letters

if uppercase_on.lower() == 'д' :
    chars += uppercase_letters

if punctuation_on.lower() == 'д' :
    chars += punctuation

if exception_on.lower() == 'д' :
    for e in exception :
        index = chars.find(e)
        chars = chars[ : index] + chars[index + 1 : ]

for i in range(pass_quantity) :
    print(generating_password(pass_lenght, chars))   
