n1, n2 = map(int, input().split())
a1 = []
a2 = []
r1, r2 = 0, 0


for i in str(n1) :
    a1.append(int(i))

for i in range(len(a1)) :
    r1 += a1[i]

for k in str(n2) :
    a2.append(int(k))


for i in range(len(a2)) :
    r2 += a2[i]
    
print(r1*r2)
