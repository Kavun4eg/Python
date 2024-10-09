while True:
    user_input = input("Введіть слово, яке містить літеру 'h': ")

    if 'h' in user_input.lower():
        print("Дякую, ви ввели слово коректно!")
        break
    else:
        print("Слово не містить літери 'h'. Спробуйте ще раз.")