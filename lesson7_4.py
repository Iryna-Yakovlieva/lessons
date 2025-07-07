# Напишіть функцію common_elements, яка згенерує два списки елементів з генераторного виразу (range) для 100 елементів,
# за наступними правилом:

# Один список з числами кратними 3, інший з кратними числами 5.
# За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
# Функція повинна повернути цю множину як результат своєї роботи.

def common_elements():
    list_3 = [numb for numb in range(100) if numb % 3 == 0]
    list_5 = [numb for numb in range(100) if numb % 5 == 0]
    return set(list_3).intersection(set(list_5))

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print(common_elements())