with open('input.txt', 'r') as file:
    data = list(file.read())

for i in range(len(data) - 3):
    if len(set(data[i:i + 4])) == 4:
        print(i + 4)
        break
