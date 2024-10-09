user_input = input("Введіть строку: ")

# count unique symbols
unique_characters = set(user_input)

# check the number of unique characters
if len(unique_characters) > 10:
    print(True)
else:
    print(False)