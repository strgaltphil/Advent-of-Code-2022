with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

sum_priorities = 0

teams = [data[i:i+3] for i in range(0, len(data), 3)]

for team in teams:
    for i in set(team[0]) & set(team[1]) & set(team[2]):
        if ord(i[0]) > 96:
            sum_priorities += ord(i) - 96
        else:
            sum_priorities += ord(i) - 38

print(sum_priorities)
