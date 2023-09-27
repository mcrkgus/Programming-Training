H, W = map(int, input().split())
num = list(map(int, input().split()))
res = 0
for i in range(1, W-1) :
    left = max(num[:i])
    right = max(num[i+1:])
    tmp = min(left, right)
    if num[i] < tmp : 
        res += tmp-num[i]
        
print(res)
