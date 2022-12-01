from itertools import groupby

with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

print(max([sum(map(int, g)) for k, g in groupby(data, key=bool) if k]))
