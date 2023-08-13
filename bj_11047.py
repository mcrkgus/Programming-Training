N, K = map(int, input().split())
cnt = 0
n_list = []

for i in range(N) :
    a = int(input())
    n_list.append(a)

for j in reversed(range(N)) :
    cnt += K // n_list[j]
    K = K % n_list[j]

print(cnt)
