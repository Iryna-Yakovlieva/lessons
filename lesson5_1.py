# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True
from string import punctuation
import keyword

user_input_string = "_"
allowed_exceptions = "_"
# Не починається з цифр
string_no_numbers = not user_input_string.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
# Перший символ у верхньому, а решта у нижньому регістрі?
string_no_register = not any(char.isupper() for char in user_input_string)
# пробіл і знаки пунктуації
string_no_character = all(
    char not in punctuation or char in allowed_exceptions
    for char in user_input_string
)
# бути жодним із зареєстрованих слів.
string_no_keywords = user_input_string not in keyword.kwlist
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
max_text = user_input_string.count('_') <= 1
no_spaces = ' ' not in user_input_string
if (
    string_no_register
    and string_no_character
    and string_no_keywords
    and string_no_numbers
    and max_text
    and no_spaces
):
    print("True")
else:
    print("False")

