# itgid.info

# Task 04
# Напишите функцию f04, получает tuple и значение и проверяет наличие значения в tuple.
#  Возвращает 'y' если значение есть и 'n' если нет.

def f04(t, v) :
    if v in t:
        return 'y'
    else:
        return 'n'


tpl = (100, 105, 110)
print(f04(tpl, 105))