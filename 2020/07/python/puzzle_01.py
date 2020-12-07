import re


def build_rules(lines):
    rules = []
    for line in lines:
        bag = re.search(r'^([\w]+ [\w]+)', line)
        content = re.findall(r'((\d) ([\w]+ [\w]+))', line)
        rules.append([bag.group(0)] + [b[2] for b in content])
    return rules


def count_bag_colors(color, rules):
    colors = set()
    for rule in rules:
        bag_color = rule[0]
        content_colors = rule[1:]

        if color in content_colors:
            colors.add(bag_color)
            colors.update(count_bag_colors(bag_color, rules))

    return colors


with open('input.txt') as f:
    lines = list(f.read().splitlines())
    rules = build_rules(lines)
    colors = count_bag_colors('shiny gold', rules)
    answer = len(colors)
    print(f'The answer is {answer}')
