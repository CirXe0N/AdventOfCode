def calculate(entries):
    total_value = 2020
    for entry_1 in entries:
        entry_1 = int(entry_1)
        entry_2 = total_value - entry_1

        if str(entry_2) in entries:
            return entry_1 * entry_2

with open('input.txt') as f:
    entries = list(f.read().splitlines())
    answer = calculate(entries)
    print(f'The answer is {answer}')
