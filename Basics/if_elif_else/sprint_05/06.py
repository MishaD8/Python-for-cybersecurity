# Task 06
# Напишите функцию f06, которая принимает число - температуру воды. Если температура ниже нуля то возвращает строку 'ice', если от 0 до 20 градусов то строку 'cold', если от 21 до 45 то 'warm', если от 46 до 99 то строку 'hot'. Если больше или равно 100 то 'steam'.

def f06(t):
   if t < 0:
      return 'ice'
   elif 0 <= t <= 20:
      return 'cold'
   elif 21 <= t <=45:
      return 'warm'
   elif 46 <= t <= 99:
      return 'hot'
   else:
      return 'steam'

print(f06(186))
