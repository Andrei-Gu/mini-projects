# Отгадываем слово по буквам - Виселица (Hangman)

# возвращает случайное слово из списка word_list в верхнем регистре
def get_word() :
    return choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(attempts):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    print(stages[attempts])

# проверка на соответствие русскому алфавиту
def is_ru(s) :
    flag = True
    for c in s.upper() :
        if ord(c) < 1040 or 1071 < ord(c):
            flag = False
            break
    return flag


# ввод и проверка буквы / слова
def guess_input(lengh) :
    while True :
        temp_guess = input('Введите букву или слово целиком: ')
        if temp_guess.isalpha() == True and is_ru(temp_guess) == True and (len(temp_guess) == 1 or len(temp_guess) == lengh) :
            return temp_guess
        else :
            print('Будьте внимательны. Введите одну букву или слово целиком на русском языке')


# логика самой игры
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    attempts = 6                       # количество попыток
    print('Давайте играть в угадайку слов! Она же виселица. Слова из руссокого языка')
    display_hangman(attempts)
    print(word_completion, 'Количество букв в слове:', len(word))

    while guessed == False and attempts > 0 :
        guess = guess_input(len(word)).upper()
        if len(guess) == 1 :
            if guess in guessed_letters :
                print('Вы уже вводили эту букву. Введите другую букву.')
            else :
                guessed_letters.append(guess)
                if guess not in word :
                    attempts -= 1
                    display_hangman(attempts)
                else :
                    for i in range(len(word)) :
                        if word[i] == guess :
                            word_completion = word_completion[ : i] + guess + word_completion[i + 1 :]
                    print(word_completion)
                    if '_' not in word_completion :
                        print('Поздравляем, вы угадали слово! Вы победили!')
                        guessed = True
                
        else :
            if guess in guessed_words :
                print('Вы уже вводили это слово. Введите другое слово.')
            else :
                guessed_words.append(guess)
                if guess != word :
                    attempts -= 1
                    display_hangman(attempts)
                else :
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    guessed = True
    if attempts == 0 :
        print('Повезет в следующий раз. Загаданное слово:', word)
            

from random import *
word_list = ['коварство', 'фюзеляж', 'палеонтолог', 'рудимент', 'охлократия', 'глобализация', 'телевидение', 'политика', 'образование', 'конференция', 'мировоззрение', 'катастрофа', 'фантастика', 'удовлетворение', 'великодушие', 'ипподром', 'сопротивление', 'космодром', 'туманность', 'грейпфрут', 'катехизис', 'медальон', 'законодательство', 'перекресток', 'иммунитет']

again = 'д' # признак для повтора игры
while again.lower() == 'д' :
    play(get_word())
    again = input('Желаете сыграть еще раз? (д = да, любой иной символ = нет): ')
print('Спасибо, что играли в угадайку слов. Еще увидимся...')
