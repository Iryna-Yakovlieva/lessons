# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

while True:
    user_input1 = float(input("Введіть перше число: "))
    user_operation = input("Введіть дію (+, -, *, /): ")
    user_input2 = float(input("Введіть друге число: "))

    # Калькулятор
    if user_operation == "+":
        result = user_input1 + user_input2
    elif user_operation == "-":
        result = user_input1 - user_input2
    elif user_operation == "*":
        result = user_input1 * user_input2
    elif user_operation == "/":
        if user_input2 != 0:
            result = user_input1 / user_input2
        else:
            result = "на 0 не ділиться"
    else:
        result = "що за знак?"
    print("Результат:", result)
    again = input("Хочеш ще одне обчислення? (так/ні): ").strip().lower()
    if again not in ("так", "y", "yes"):
        print("👋 Дякую! Пока пока")
        break



