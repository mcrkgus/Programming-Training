from itertools import combinations

N, M = map(int, input().split())
city = []
chicken = []
house = []
result = 999999
for i in range(N) :
    s = list(map(int, input().split()))
    city.append(s)

for i in range(N) :
    for j in range(N) :
        if city[i][j] == 2 :
            chicken.append([i, j])
        elif city[i][j] == 1 :
            house.append([i, j])
            
for i in combinations(chicken, M) :
    temp = 0
    for j in house :
        r1, c1 = j 
        chicken_distance = 1000
        for k in i :
            r2, c2 = k
            chicken_distance = min(chicken_distance, abs(r1-r2) + abs(c1-c2))
        temp += chicken_distance
    
    result = min(result, temp)
    
print(result)
