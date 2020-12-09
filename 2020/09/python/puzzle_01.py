def find_number(preamble_amount, numbers):
    number = 0
    index = preamble_amount

    while index < len(numbers):
        preamble = numbers[index - preamble_amount:index]
        number = numbers[index]
        is_valid = any([number - y in preamble for y in preamble])

        if not is_valid:
            break

        index += 1

    return number


with open('input.txt') as f:
    numbers = list(map(int, f))
    answer = find_number(25, numbers)
    print(f'The answer is {answer}')
