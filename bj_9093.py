T = int(input())

for i in range(T) :
    s = list(input().split())
    for j in s :
        print(j[::-1], end=" ")
