with open('input.txt', 'r') as file:
    data = [(line.split()) for line in file.read().split('\n')]


def get_score(opponent, you):
    your_shape_score = 0

    if you == 'X':
        your_shape_score = 1
    elif you == 'Y':
        your_shape_score = 2
    else:
        your_shape_score = 3

    if opponent == 'A' and you == 'X' or opponent == 'B' and you == 'Y' or opponent == 'C' and you == 'Z':
        return 3 + your_shape_score
    elif opponent == 'A' and you == 'Y' or opponent == 'B' and you == 'Z' or opponent == 'C' and you == 'X':
        return 6 + your_shape_score
    else:
        return your_shape_score


print(sum([get_score(*d) for d in data]))
