with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

setup_data = data[:data.index('') - 1]
setup_data.reverse()

crate_stacks = list()

def pop_n(stack ,n):
    for _ in range(n):
        yield crate_stacks[stack].pop()

for d in setup_data:
    crates = d.split(' ')

    while crates.count('') > 0:
        index = crates.index('')
        crates[index:index+4] = [None]

    if len(crate_stacks) == 0:
        for i in range(len(crates)):
            crate_stacks.append([])

    for index, crate in enumerate(crates):
        if crate is not None:
            crate_stacks[index].append(crate)

for d in data[data.index('') + 1:]:
    _, quantity, _, start, _, end = d.split()
    crate_stacks[int(end) - 1].extend(list(pop_n(int(start) - 1, int(quantity))))

for c in crate_stacks:
    print(c[-1].replace('[', '').replace(']', ''), end='')