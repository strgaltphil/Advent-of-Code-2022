with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

sum_priorities = 0

for line in data:
    items = list(line)

    for i in set(items[:(len(items)//2)]) & set(items[len(items)//2:]):
        if ord(i[0]) > 96:
            sum_priorities += ord(i) - 96
        else:
            sum_priorities += ord(i) - 38

print(sum_priorities)