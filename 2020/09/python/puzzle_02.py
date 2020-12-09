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


def find_encryption_weakness(number, numbers):
    contiguous_range = []
    index = 0

    while index < numbers.index(number):
        sum_values = 0
        contiguous_range = []

        idx = index
        while sum_values < number:
            sum_values += numbers[idx]
            contiguous_range.append(numbers[idx])
            idx += 1

        if sum_values == number:
            break

        index += 1

    return max(contiguous_range) + min(contiguous_range)


with open('input.txt') as f:
    numbers = list(map(int, f))
    number = find_number(25, numbers)
    answer = find_encryption_weakness(number, numbers)
    print(f'The answer is {answer}')
