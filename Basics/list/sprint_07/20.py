# itgid.info - python 2023

# Напишите функцию f20, которая получает list и возвращает сумму элементов
#  с четными индексами. Подсказка - посмотрите sprint по циклам!!!


# write your code under this line
def f20 (ct) :
    i = 0
    count = 0
    while i < len(ct):
        count += ct[i]
        i += 2
    return count


list1 = [5, 6, 7, 8]

s = f20(list1)
print(s) # ожидаю 12