with open('input.txt', 'r') as file:
    data = [list(map(int, f)) for f in file.read().split('\n')]


dimension = len(data)


def get_up(x, y):
    return [i[x] for i in data][:y][::-1]


def get_right(x, y):
    return data[y][x+1:]


def get_down(x, y):
    return [i[x] for i in data][y+1:]


def get_left(x, y):
    return data[y][:x][::-1]


def get_viewing_distance(l, height):
    if not len(l):
        return 0

    n = 0
    for t in l:
        if t >= height:
            return n + 1
        n += 1
    return n


def get_scenic_score(x, y):
    du = get_viewing_distance(get_up(x, y), data[y][x])
    dr = get_viewing_distance(get_right(x, y), data[y][x])
    dd = get_viewing_distance(get_down(x, y), data[y][x])
    dl = get_viewing_distance(get_left(x, y), data[y][x])

    return du*dr*dd*dl


print(max([get_scenic_score(i % dimension, i // dimension)
      for i in range(dimension ** 2)]))
