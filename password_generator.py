import random
from random import choice
import time
import os
import sys

list1 = []

def hello():
    print('Привет! Я программа, для генерации паролей!')


def fast_password():
    fast = input('Быстрая генерация пароля(без дополнительных настроек) Напиши "да" или "нет":')
    fast = fast.strip()
    while fast.lower() not in ['да', 'нет']:
        print('Нужно вводить ДА или НЕТ.')
        fast = input('Быстрая генерация пароля(без дополнительных настроек) Напиши "да" или "нет":')
    return fast


def count():
    if fast == "нет":
        num = input('Какое КОЛЛИЧЕСТВО паролей мне создать?! Напиши цифру!:')
        while num.isdigit() == False:
            print('Нужно вести цифру.')
            num = input('Какое КОЛЛИЧЕСТВО паролей мне создать?! Укажи цифру!:')
        return int(num)
    else:
        return (1)

def password_length():
    if fast == "нет":
        leen = input('Какая будет ДЛИНА пароля(кол-во символов)?! Напиши цифру!:')
        while leen.isdigit() == False:
            print('Нужно вести цифру.')
            leen = input('Какая будет ДЛИНА пароля?! Напиши цифру!:')
        return int(leen)
    else:
        return (18)

def numbers():
    numm = input('Включать в пароль ЦИФРЫ >0123456789< ?! Напиши "да" или "нет":')
    numm = numm.strip()
    while numm.lower() not in ['да', 'нет']:
        print('Нужно вводить ДА или НЕТ.')
        numm = input('Включать в пароль ЦИФРЫ >0123456789< ?! Напиши "да" или "нет":')
    return numm

def capital_letters():
    nupper = input('Включать в пароль ЗАГЛАВНЫЕ >ABCDEFGHIJKLMNOPQRSTUVWXYZ< буквы?! Напиши "да" или "нет":')
    nupper = nupper.strip()
    while nupper.lower() not in ['да', 'нет']:
        print('Нужно вводить ДА или НЕТ.')
        nupper = input('Включать в пароль ЗАГЛАВНЫЕ >ABCDEFGHIJKLMNOPQRSTUVWXYZ< буквы?! Напиши "да" или "нет":')
    return nupper

def lower_case():
    num_lower = input('Включать в пароль СТРОЧНЫЕ >abcdefghijklmnopqrstuvwxyz< буквы?! Напиши "да" или "нет":')
    num_lower = num_lower.strip()
    while num_lower.lower() not in ['да', 'нет']:
        print('Нужно вводить ДА или НЕТ.')
        num_lower = input('Включать в пароль СТРОЧНЫЕ >abcdefghijklmnopqrstuvwxyz< буквы?! Напиши "да" или "нет":')
    return num_lower

def symbols():
    unclear = input('Включать в пароль символы  !#$%&*+-=?@^_  ?! Напиши "да" или "нет":')
    unclear = unclear.strip()
    while unclear.lower() not in ['да', 'нет']:
        print('Нужно вводить ДА или НЕТ.')
        unclear = input('Включать в пароль символы  !#$%&*+-=?@^_  ?! Напиши "да" или "нет":')
    return unclear

def  ambiguous_characters():
    amb = input('Исключать ли неоднозначные символы  il1Lo0O  ?! Напиши "да"(Не исключать) или "нет"(Исключать):')
    amb = amb.strip()
    while amb.lower() not in ['да', 'нет']:
        print('Нужно вводить ДА или НЕТ.')
        amb = input('Исключать ли неоднозначные символы  il1Lo0O  ?! Напиши "да(НЕ исключать)" или "нет(Исключать)":')
    return amb



def gen_chars():
    chars = ''
    if fast == 'да':
        chars += '0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '!#$%&*+-=?@^_' + 'il1Lo0O'
        return chars
    else:
        if numm == 'да':
            chars += '0123456789'
        if nupper == 'да':
            chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if num_lower == 'да':
            chars += 'abcdefghijklmnopqrstuvwxyz'
        if unclear == 'да':
            chars += '!#$%&*+-=?@^_'
        if amb == 'да':
            chars += 'il1Lo0O'
        return chars

list1 == []

def generate_password():
    if chars != '':
        for i in range(num):
            password = []
            for j in range(leen):
                password.append(choice(chars))
            print(''.join(password))
            list1.append(''.join(password))

        return password
    else:
        noy_password()




def noy_password():

    print('Пароль не создан!')

def write_passwort():
    if chars != '':
        passs = input('Мне сохранять пароль?:')
        passs = passs.strip()
        while passs.lower() not in ['да', 'нет']:
            print('Нужно вводить ДА или НЕТ.')
            passs = input('Мне сохранять пароль?:')
        return passs

def cloysed():
    a = 0
    for x in range(0, 6):
        a = a + 1
        b = ("Программа завершает работу" + "." * a)
        # \r prints a carriage return first, so `b` is printed on top of the previous line.
        sys.stdout.write('\r' + b)
        time.sleep(5)
    print(a)


def passy():
    if chars != '' and passs == 'да':
        try:
            # Получаем путь к рабочему столу независимо от версии Windows
            homeDir = os.path.expanduser('~')

            # Все возможные пути к рабочему столу (включая OneDrive)
            possible_desktop_paths = [
                os.path.join(homeDir, 'OneDrive', 'Рабочий стол'),  # W11 + OneDrive (рус)
                os.path.join(homeDir, 'OneDrive', 'Desktop'),  # W11 + OneDrive (англ)
                os.path.join(homeDir, 'Desktop'),  # Обычный английский
                os.path.join(homeDir, 'Рабочий стол'),  # Обычный русский
            ]

            desktop_path = None
            for path in possible_desktop_paths:
                if os.path.exists(path) and os.path.isdir(path):
                    desktop_path = path
                    break

            # Если не нашли ни одну папку, создаем Desktop в домашней папке
            if desktop_path is None:
                desktop_path = os.path.join(homeDir, 'Desktop')
                os.makedirs(desktop_path, exist_ok=True)
                print(f"Создана папка Desktop: {desktop_path}")

            # Создаем полный путь к файлу
            file_path = os.path.join(desktop_path, 'Пароли(Password generator).txt')

            # Открываем файл для добавления данных
            with open(file_path, "a", encoding='utf-8') as file:
                # Проверяем, пустой ли файл
                file.seek(0, 2)  # Переходим в конец файла
                if file.tell() == 0:  # Если позиция = 0, файл пуст
                    file.write('НЕ ИЗМЕНЯЙ НАЗВАНИЕ ФАЙЛА!\n')
                    file.write('=' * 40 + '\n')

                # Записываем все пароли
                for password in list1:
                    file.write(password + '\n')
                file.write('=' * 40 + '\n')
                file.write(f'Сгенерировано: {time.strftime("%Y-%m-%d %H:%M:%S")}\n\n')

            print(f'Пароли успешно сохранены!\nПуть: {file_path}')

        except Exception as e:
            print(f'Ошибка при сохранении файла: {e}')
            print('Пароли, которые не удалось сохранить:')
            for password in list1:
                print(password)
    elif passs == 'нет':
        print('Пароли не сохранены. Возвращайся!')




hello()
time.sleep(0.5)
fast = fast_password()
num = count()
leen = password_length()
if fast == 'да':
    chars = gen_chars()
    print('Создаю...')
    #time.sleep(3)
    password = generate_password()
    time.sleep(0.5)
    passs = write_passwort()
    passy()
    time.sleep(0.5)
    cloysed()
else:
    numm = numbers()
    nupper = capital_letters()
    num_lower = lower_case()
    unclear = symbols()
    amb = ambiguous_characters()
    chars = gen_chars()
    print('Создаю...')
    time.sleep(1.4)
    password = generate_password()
    time.sleep(1)
    passs = write_passwort()
    passy()
    time.sleep(0.5)
    cloysed()



