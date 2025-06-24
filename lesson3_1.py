user_input1 = float(input("Введіть перше число: "))
user_operation = input("Введіть дію (+, -, *, /): ")
user_input2 = float(input("Введіть друге число: "))

# Калькулятор
if user_operation == "+":
    resalt = user_input1 + user_input2
elif user_operation == "-":
    resalt = user_input1 - user_input2
elif user_operation == "*":
    resalt = user_input1 * user_input2
elif user_operation == "/":
    if user_input2 != 0:
        resalt = user_input1 / user_input2
    else:
        resalt = "на 0 не ділиться"
print("Результат:", resalt)


