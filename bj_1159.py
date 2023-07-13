N = int(input())
name = [list(input()) for _ in range(N)]
player_list = []
result = []

for i in range(N) :
    player_list.append(name[i][0])

first_name = set(player_list)
for i in first_name :
    if player_list.count(i) >= 5 :
        result.append(i)

if len(result) == 0 :
    print("PREDAJA")
else :
    print(''.join(sorted(result)))
