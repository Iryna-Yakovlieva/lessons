# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string, у якому є string.ascii_letters, з усім набором потрібних букв
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

user_input_string = input("діапазон: ")
letter_1 = user_input_string[0]
letter_2 = user_input_string[-1]
oll_letters = string.ascii_letters

start_index = oll_letters.index(letter_1)
end_index = oll_letters.index(letter_2)
result = oll_letters[start_index:end_index + 1]
print(result)
