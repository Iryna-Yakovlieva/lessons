user_input = int(input("Введіть ціле 4-х значне число: "))
n1 = user_input // 1000
n2 = (user_input % 1000) // 100
n3 = (user_input % 100) // 10
n4 = user_input % 10
print(n1, n2, n3, n4, sep='\n')