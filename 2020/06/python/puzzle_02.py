from collections import Counter


def sum_counts(groups):
    counts = []
    for group in groups:
        persons = group.split('\n')

        counter = Counter(persons[0])

        for person in persons:
            counter = counter & Counter(person)

        counts.append(len(counter))

    return sum(counts)


with open('input.txt') as f:
    groups = f.read().split(sep='\n\n')
    answer = sum_counts(groups)
    print(f'The answer is {answer}')
