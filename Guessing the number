# Угадайка чисел

print('Добро пожаловать в числовую угадайку!')

# проверка введенного значения для правой границы
def is_valid_limit(s) :
    return s.isdigit() and int(s) > 1

# ввод значения правой границы
def inputing_right_limit() :
    right_limit = 0
    while right_limit <= 1 :
        right_limit_temp = input('Введите правую границу для случайного выбора числа от 1 до n включительно): ')
        if is_valid_limit(right_limit_temp) == False :
            print('Это должно быть целое число больше 1')
        else :
            return int(right_limit_temp)

# проверка введенного пользователем значения при угадывании
def is_valid(s, n) :
    return s.isdigit() and 1<= int(s) <= n

# сама угадайка
def guessing_num(right_limit) :
    num = randint(1, right_limit)
    flag = True
    attempts = 0 # счетчик попыток пользователя
    while flag == True :
        num_guess = input('Введите число в заданном диапазоне ')
        if is_valid(num_guess, right_limit) == False :
            print('Всё-таки необходимо именно целое число от 1 до', right_limit)
        else :
            attempts += 1
            num_guess = int(num_guess)
            if num == num_guess :
                flag = False
                print('Вы угадали, поздравляем! Количество попыток:', attempts)
            elif num > num_guess :
                print('Слишком мало, попробуйте еще раз')
            else :
                print('Слишком много, попробуйте еще раз')


from random import *
again = 'д' # признак для повтора игры
while again.lower() == 'д' :
    guessing_num(inputing_right_limit())
    again = input('Желаете сыграть еще раз? (д = да, н = нет): ')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
