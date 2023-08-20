N = int(input())
info = []
cnt = 0

for i in range(N) :
    start, end = map(int, input().split())
    info.append([start, end])


info = sorted(info, key=lambda a: a[0]) 
info = sorted(info, key=lambda a: a[1]) 

current_time = 0
for i, j in info :
    if i >= current_time :
        cnt += 1
        current_time = j

print(cnt)
