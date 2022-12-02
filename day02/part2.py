with open('input.txt', 'r') as file:
    data = [(line.split()) for line in file.read().split('\n')]


# rock = 1
# paper = 2
# scissor = 3
def get_score(opponent, round):
    if round == 'X':
        if opponent == 'A':
            return 3
        elif opponent == 'B':
            return 1
        else:
            return 2
    elif round == 'Y':
        if opponent == 'A':
            return 4
        elif opponent == 'B':
            return 5
        else:
            return 6
    else:
        if opponent == 'A':
            return 8
        elif opponent == 'B':
            return 9
        else:
            return 7


print(sum([get_score(*d) for d in data]))
