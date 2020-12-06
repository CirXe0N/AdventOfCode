import math


def determine_max_seat_id(lines):
    seat_ids = []
    for line in lines:
        row = decode_row_position(line[:7])
        column = decode_column_position(line[7:])
        seat_id = (row * 8) + column
        seat_ids.append(seat_id)

    return max(seat_ids)


def decode_row_position(code):
    rows = range(128)

    for letter in code:
        separator = math.floor(len(rows) / 2)
        rows = rows[:separator] if letter == 'F' else rows[separator:]

    return rows[0]


def decode_column_position(code):
    cols = range(8)

    for letter in code:
        separator = math.floor(len(cols) / 2)
        cols = cols[:separator] if letter == 'L' else cols[separator:]

    return cols[0]


with open('input.txt') as f:
    lines = list(f.read().splitlines())
    answer = determine_max_seat_id(lines)
    print(f'The answer is {answer}')
