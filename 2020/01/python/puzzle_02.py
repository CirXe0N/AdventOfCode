def calculate(entries):
    total_value = 2020

    for entry_1 in entries:
        entry_1 = int(entry_1)

        for entry_2 in entries:
            entry_2 = int(entry_2)

            entry_3 = total_value - entry_2 - entry_1

            if str(entry_3) in entries:
                return entry_1 * entry_2 * entry_3

    print(entries)

with open('input.txt') as f:
    entries = list(f.read().splitlines())
    answer = calculate(entries)
    print(f'The answer is {answer}')
