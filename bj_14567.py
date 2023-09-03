import sys
input = sys.stdin.readline     
N, M = map(int, input().split())
semester = [1] * (N+1)
subject = []
for i in range(M) :
    A, B = map(int, input().split())
    subject.append((A, B))
subject.sort()
for a, b in subject :
    if semester[b] <= semester[a] :
        semester[b] = semester[a]+1


for i in  range(1, len(semester)) :
    print(semester[i], end=" ")
