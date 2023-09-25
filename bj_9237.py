N = int(input())
growth = list(map(int, input().split()))
growth.sort(reverse=True)

for i in range(len(growth)) :
    growth[i] += (i+1)
    
res = max(growth) + 1
