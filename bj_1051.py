n, m = map(int, input().split())
arr = []
res = []
for i in range(n) :
    a = list(map(int, input()))
    arr.append(a)
    
for i in range(n) :
    for j in range(m) :
        cur = arr[i][j]
        for k in range(j, m) :
            if cur == arr[i][k] :
                gap = k-j
                if i+gap < n and j+gap <m :
                    if cur == arr[i+gap][j] and cur == arr[i+gap][j+gap] :
                        res.append((gap+1)*(gap+1))
#print(res)
print(max(res))
