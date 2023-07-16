A, B = map(int, input().split())
num = []
sum = 0

for i in range(1, 100, 1) :
    for k in range(i) :
        num.append(i)

for i in range(A-1, B) :
    sum += num[i]
    
print(sum)
