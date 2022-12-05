with open('input.txt', 'r') as file:
    data = [[list(map(int, l.split('-'))) for l in line.split(',')] for line in file.read().split('\n')]

overlapping_spaces = 0

for d in data:
    first_elve = set(range(d[0][0], d[0][1] + 1))
    second_elve = set(range(d[1][0], d[1][1] + 1))
    intersection = first_elve & second_elve

    if intersection != set():
        overlapping_spaces += 1

print(overlapping_spaces)