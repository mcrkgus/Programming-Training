info = []
rank = 0

N = int(input())
for _ in range(N) :
    x, y = map(int, input().split())
    info.append((x, y))



for i in info :
    rank = 1
    for j in info :
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")

