from collections import defaultdict

with open('input.txt', 'r') as file:
    data = [f.split() for f in file.read().split('\n')]


full_path = []
directory_sizes = defaultdict(int)

for d in data:
    if d[0] == '$':
        if d[1] == 'cd':
            if d[2] == '..':
                full_path.pop()
            else:
                full_path.append(d[2])
    else:
        if d[0] != 'dir':
            for i in range(len(full_path)):
                directory_sizes['/'.join(full_path[:i+1])] += int(d[0])

free_space = 70000000 - directory_sizes['/']
space_needed = 30000000 - free_space

deletable = []
for value in directory_sizes.values():
    if (value > space_needed):
        deletable.append(value)

print(min(deletable))
