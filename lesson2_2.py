user_input = int(input("Введіть ціле 5-ти значне число: "))
print(user_input)

n1 = user_input % 10
user_input = user_input // 10

n2 = user_input % 10
user_input = user_input // 10

n3 = user_input % 10
user_input = user_input // 10

n4 = user_input % 10
user_input = user_input // 10

n5 = user_input % 10

user_result = (
    n1 * 10000 +
    n2 * 1000 +
    n3 * 100 +
    n4 * 10 +
    n5
)

print(user_result)





