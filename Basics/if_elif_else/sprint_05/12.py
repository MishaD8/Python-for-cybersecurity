# Task 12
# Напишите функцию f12 которая принимает строку и возвращает:
# еслих входящая строка 'http' или 'https' то возвращает строку 'url'
# если входящая строка '@' то возвращает 'email'
# если входящая строка 'ftp' то возвращает 'ftp'
# во всех остальных случаях - возвращает пустую строку

def f12(s):
    if s == 'http' or s == 'https':
        return 'url'
    elif s == '@':
        return 'email'
    elif s == 'ftp':
        return 'ftp'
    else:
        return ''

print(f12('http'))