def find_unique_value(some_list: list) -> list:
	for numb in list(some_list):
		if some_list.count(numb) == 1:
			return numb
	return list(some_list)
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")