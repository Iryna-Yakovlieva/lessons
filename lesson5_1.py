# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# # Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

from string import punctuation
import keyword
user_input_string = input("Введіть вираз: ")
allowed_exceptions = "_"
# Не починається з цифр
string_no_numbers = not (user_input_string and user_input_string[0].isdigit())
# Не містити великі літери
string_no_register = not any(char.isupper() for char in user_input_string)
# Змінна не може пробіл і знаки пунктуації, окрім нижнього підкреслення "_".
no_spaces = ' ' not in user_input_string
string_no_character = all(
    char not in punctuation or char in allowed_exceptions
    for char in user_input_string
)
# бути жодним із зареєстрованих слів.
string_no_keywords = user_input_string not in keyword.kwlist
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_". Уточнення підряд!!
max_text = user_input_string.count('_' * 2) <= 0
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

