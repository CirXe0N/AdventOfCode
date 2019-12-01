import math


def calculate_fuel(amount: int) -> int:
    return math.floor(amount / 3) - 2


def calculate_module_fuel(mass: int) -> int:
    fuel = mass
    module_fuel = 0

    while fuel > 0:
        fuel = calculate_fuel(fuel)
        module_fuel += fuel if fuel > 0 else 0

    return module_fuel


total_fuel = 0
with open('input.txt') as f:
    for line in f.readlines():
        total_fuel += calculate_module_fuel(int(line))


print(f'The answer is {total_fuel}')
