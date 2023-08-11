N = int(input())
num = list(map(int, input().split()))
max_num = num[0]
min_num = num[0]
for i in num[1:]:
    if i > max_num :
        max_num = i
    elif i < min_num :
        min_num = i
print(min_num, max_num)
