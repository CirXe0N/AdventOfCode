import re


def build_rules(lines):
    rules = {}
    for line in lines:
        bag_color = re.search(r'^([\w]+ [\w]+)', line).group(0)
        content = re.findall(r'((\d) ([\w]+ [\w]+))', line)

        bag = {}
        for item in content:
            bag[item[2]] = int(item[1])

        rules[bag_color] = bag

    return rules


def count_bags(color, rules):
    bag = rules[color]

    count = 0
    for k, v in bag.items():
        for n in range(v):
            count += 1 + count_bags(k, rules)

    return count


with open('input.txt') as f:
    lines = list(f.read().splitlines())
    rules = build_rules(lines)
    answer = count_bags('shiny gold', rules)
    print(f'The answer is {answer}')
