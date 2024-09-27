# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = [char for char in alice_in_wonderland if char == "'"]
print(single_quotes)  # Output: ['\'', '\'', '\'', '\'']

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

# task 04
black_sea_area = 436402  # km²
azov_sea_area = 37800  # km²
total_area = black_sea_area + azov_sea_area
print(f"The total area of the Black Sea and the Azov Sea is {total_area} km².")

# task 05
total_items = 375291
first_second = 250449
second_third = 222950

# Let A be items in warehouse 1, B in warehouse 2, C in warehouse 3
# A + B + C = 375291
# A + B = 250449
# B + C = 222950

A = 250449 - (375291 - 222950)
B = 250449 - A
C = 375291 - A - B

A = 103099
B = 147350
C = 124842

print(f"Warehouse 1 has {A}, Warehouse 2 has {B}, Warehouse 3 has {C} items.")

# task 06
monthly_payment = 1179  # UAH
months = 1.5 * 12  # 1.5 years in months
total_cost = monthly_payment * months
print(f"The total cost of the computer is {total_cost} UAH.")

# task 07
numbers = [8019, 9907, 2789, 7248, 7128, 19224]
divisors = [8, 9, 5, 6, 5, 9]
remainders = [n % d for n, d in zip(numbers, divisors)]
print(f"The remainders are: {remainders}")

# task 08
order = {
    "Піца велика": (4, 274),
    "Піца середня": (2, 218),
    "Сік": (4, 35),
    "Торт": (1, 350),
    "Вода": (3, 21),
}

total_cost = sum(quantity * price for quantity, price in order.values())
print(f"The total cost for Iryna's order is {total_cost} UAH.")

# task 09
total_photos = 232
photos_per_page = 8
pages_needed = -(-total_photos // photos_per_page)  # Ceiling division
print(f"Igor needs {pages_needed} pages for his photos.")

# task 10
distance = 1600  # km
fuel_per_100km = 9  # liters
tank_capacity = 48  # liters

# Total fuel needed
total_fuel_needed = (distance / 100) * fuel_per_100km
# Number of refuels needed
refuels_needed = -(-total_fuel_needed // tank_capacity)  # Ceiling division

print(f"The family will need {total_fuel_needed} liters of fuel.")
print(f"They will need to refuel at least {refuels_needed} times.")
