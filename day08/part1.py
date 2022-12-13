with open('input.txt', 'r') as file:
    data = [list(map(int, f)) for f in file.read().split('\n')]


dimension = len(data)


def get_up(x, y):
    return [i[x] for i in data][:y]


def get_right(x, y):
    return data[y][x+1:]


def get_down(x, y):
    return [i[x] for i in data][y+1:]


def get_left(x, y):
    return data[y][:x]


visible_trees = set()

for y in range(1, dimension - 1):
    for x in range(1, dimension - 1):
        up = [data[y][x] > t for t in get_up(x, y)]
        right = [data[y][x] > t for t in get_right(x, y)]
        down = [data[y][x] > t for t in get_down(x, y)]
        left = [data[y][x] > t for t in get_left(x, y)]

        if any(map(all, [up, right, down, left])):
            visible_trees.add((x, y))

print(len(visible_trees) + 2 * dimension + 2 * (dimension - 2))
