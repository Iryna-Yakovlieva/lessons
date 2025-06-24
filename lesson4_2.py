
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
#
# [1, 3, 5] => 30
# [6] => 36
# [] => 0

first_list = [0, 1, 7, 2, 4, 8]
if len(first_list) == 0:
    new_lst2 = 0
else:
    new_lst = first_list[::2]
    sum_list = 0
    for item in new_lst:
        sum_list += item
    new_lst2 = sum_list * first_list[-1]
print(first_list,"->", new_lst2)
