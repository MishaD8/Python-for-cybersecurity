# itgid.info

# Task 07
# Напишите функцию f07 которая получает tuple и значение. 
# Функция проверяет есть ли значение в tuple, если есть - возвращает tuple без изменений.
#  Если значения в tuple нет, то добавляет его и возвращает новый tuple с добавленным значением.

def f07(t, v) :
    if v in t:
        return t
    else:
        return t + (v,)


tpl = (100, 105, 110)

res = f07(tpl, 115) # ожидаю (100, 105, 110, 115)

print(res)