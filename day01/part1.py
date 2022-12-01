from itertools import groupby

with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

print(max([sum(list(int(i) for i in g)) for k, g in groupby(data, key=bool) if k]))
