# ДЗ 3.3. Розділити один список на два списки у Python
#[1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
#[1, 2, 3] => [[1, 2], [3]]
#[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
#[1] => [[1], []]
#[] => [[], []]

first_list = [1, 2, 3, 4, 5, 6]
my_list1 = first_list[:3]
my_list2 = first_list[3:]
size_list = len(first_list)
middle = size_list // 2
if size_list % 2 != 0:
    middle += 1
my_list1 = first_list[:middle]
my_list2 = first_list[middle:]
print([my_list1,my_list2])




