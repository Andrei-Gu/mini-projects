# Шифр Цезаря

# проверка выбранного действия
def is_valid_action() :
    while True :
        action_temp = input('Выберете режим (0 = шифрование, 1 = дешифрование): ')
        if (action_temp.isdigit() and 0 <= int(action_temp) <= 1) == False :
            print('Введите корректное значение')
        else :
            return int(action_temp)

# проверка введенного языка
def is_valid_lang() :
    while True :
        lang_temp = input('Введите язык текста (ru = русский, en = английский): ')
        if lang_temp == 'ru' or lang_temp == 'en' :
            return lang_temp
        else :
            print('Введите корректное значение')


# ввод и проверка сдвига 
def is_valid_shift(lang) :
    while True:
        if lang == 'ru' :
            rot_temp = input('Введите значение сдвига от 1 до 31 включительно: ')
            if (rot_temp.isdigit() and 0 < int(rot_temp) < 32) == False :
                print('Введите корректное значение')
            else :
                return int(rot_temp)

        if lang == 'en' :
            rot_temp = input('Введите значение сдвига от 1 до 25 включительно: ')
            if (rot_temp.isdigit() and 0 < int(rot_temp) < 26) == False :
                print('Введите корректное значение')
            else :
                return int(rot_temp)


# замена буквы ё/Ё на е/Е
def replace_e(s) :
    if 'ё' in s :
        s = s.replace('ё','е')
    if 'Ё' in s :
        s = s.replace('Ё', 'Е')
    return s


# дешифрование (сдвиг влево)
def decryption(text, lang, rot_n) :
    if lang == 'ru' :
        text = replace_e(text)
        for i in range(len(text)) :
            if text[i] in exceptions :
                continue
            else :
                ord_i = ord(text[i])
                if 1040 <= ord_i <= 1071 : # чтобы сохранить регистр букв (А)
                    ord_i -= rot_n
                    if ord_i < 1040 :
                        ord_i = 1072 - (1040 - ord_i)
                if 1072 <= ord_i <= 1103 : # чтобы сохранить регистр букв (а)
                    ord_i -= rot_n
                    if ord_i < 1072 :
                        ord_i = 1104 - (1072 - ord_i)
                text = text[ : i] + chr(ord_i) + text[i + 1 : ]

    if lang == 'en' :
        for i in range(len(text)) :
            if text[i] in exceptions :
                continue
            else :
                ord_i = ord(text[i])
                if 65 <= ord_i <= 90 : # чтобы сохранить регистр букв (A)
                    ord_i -= rot_n
                    if ord_i < 65 :
                        ord_i = 91 - (65 - ord_i)
                if 97 <= ord_i <= 122 : # чтобы сохранить регистр букв (a)
                    ord_i -= rot_n
                    if ord_i < 97 :
                        ord_i = 123 - (97 - ord_i)
                text = text[ : i] + chr(ord_i) + text[i + 1 : ]
    print(text)


# шифрование (сдвиг вправо)
def encryption(text, lang, rot_n) :
    if lang == 'ru' :
        text = replace_e(text)
        for i in range(len(text)) :
            if text[i] in exceptions :
                continue
            else :
                ord_i = ord(text[i])
                if 1040 <= ord_i <= 1071 : # чтобы сохранить регистр букв (А)
                    ord_i += rot_n
                    if ord_i > 1071 :
                        ord_i = 1039 + (ord_i - 1071)
                if 1072 <= ord_i <= 1103 : # чтобы сохранить регистр букв (а)
                    ord_i += rot_n
                    if ord_i > 1103 :
                        ord_i = 1071 + (ord_i - 1103)
                text = text[ : i] + chr(ord_i) + text[i + 1 : ]

    if lang == 'en' :
        for i in range(len(text)) :
            if text[i] in exceptions :
                continue
            else :
                ord_i = ord(text[i])
                if 65 <= ord_i <= 90 : # чтобы сохранить регистр букв (A)
                    ord_i += rot_n
                    if ord_i > 90 :
                        ord_i = 64 + (ord_i - 90)
                if 97 <= ord_i <= 122 : # чтобы сохранить регистр букв (a)
                    ord_i += rot_n
                    if ord_i > 122 :
                        ord_i = 96 + (ord_i - 122)
                text = text[ : i] + chr(ord_i) + text[i + 1 : ]
    print(text)



exceptions = '!#$%&*+-=?@^_ 0123456789,.' # Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются

print('Шифр Цезаря!')

action = is_valid_action()
lang = is_valid_lang()
rot_n = is_valid_shift(lang)
text = input('Введите Ваш текст: ')
if action == 0 :
    encryption(text, lang, rot_n)
else :
    decryption(text, lang, rot_n)
