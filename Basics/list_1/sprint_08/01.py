# itgid.info - python 2023

# Напишите функцию f01, которая принимает аргумент - list, 
# и возвращает сумму его элементов. Решите с помощью цикла.

# write your code under this line

def f01 (f) :
    i = 0
    count = 0
    while i < len(f):
        count += f[i]
        i += 1
    return count


b = [ 11, -3, 4, 12, 7, -8]
result = f01(b)
print (result)


def f001(f) :
    count = 0
    for item in f:
        count += item
    return count

b = [11, -3, 4, 12, 7, -8]
result001 = f001(b)
print (result001)