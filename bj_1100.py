chess = [input() for _ in range(8)]
cnt = 0
for y in range(8):
    for x in range(8):
        if y%2 == x%2 and chess[y][x] == 'F':
            cnt += 1

print(cnt)
