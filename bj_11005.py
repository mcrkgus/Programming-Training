N, B = map(int, input().split())
res = ""
v = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N != 0 :
    res += str(v[N%B])
    N  = N // B
print(res[::-1])
