import math


def calculate_fuel_from_mass(mass: int) -> int:
    return math.floor(mass / 3) - 2


total_fuel = 0
with open('input.txt') as f:
    for line in f.readlines():
        total_fuel += calculate_fuel_from_mass(int(line))

print(f'The answer is {total_fuel}')
