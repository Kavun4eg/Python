# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_(a, b):
    return a+b
result = sum_(1, 2)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def seredne_arifmetychne(chysla):
    return sum(chysla) / len(chysla)

list_of_numbers = [1, 2, 3, 4, 5]
result = seredne_arifmetychne(list_of_numbers)
print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revert_text(text):
    return text[::-1]

result = revert_text("Privet kak dela")
print(result)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    if not words:
        return None
    return max(words, key=len)

list_of_words = ["Sandora", "Jaffa", "Rich", "Galicia"]
result = longest_word(list_of_words)
print(result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
# 6.3
def filter_strings(lst):
    return [item for item in lst if isinstance(item, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings(lst1)

print(lst2)

# task 8
# 6.4
def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers)

print(result)

# task 9
# 6.2
def get_word_with_h():
    while True:
        user_input = input("Введіть слово, яке містить літеру 'h': ")

        if 'h' in user_input.lower():
            print("Дякую, ви ввели слово коректно!")
            break
        else:
            print("Слово не містить літери 'h'. Спробуйте ще раз.")

get_word_with_h()

# task 10
# 6.1
def has_more_than_ten_unique_characters(input_string):

    unique_characters = set(input_string)

    return len(unique_characters) > 10

user_input = input("Введіть строку: ")
result = has_more_than_ten_unique_characters(user_input)

print(result)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


