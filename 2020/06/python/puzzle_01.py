def sum_counts(groups):
    counts = []
    for group in groups:
        group = group.replace('\n', '')
        count = len(set(group))
        counts.append(count)

    return sum(counts)


with open('input.txt') as f:
    groups = f.read().split(sep='\n\n')
    answer = sum_counts(groups)
    print(f'The answer is {answer}')
