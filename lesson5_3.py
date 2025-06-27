# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

from string import punctuation

user_input_string = input("Введіть вираз для hashtag: ")
_string = "".join(character for character in user_input_string if character not in punctuation)
my_string1 = "#" + _string.title().replace(' ', '')
max_text = 140
if len(my_string1) > max_text:
    my_string1 = my_string1[:max_text]

print(my_string1)
