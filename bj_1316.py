N = int(input())
cnt = 0
for i in range(N) :
    word = input()
    res = True

    for j in range(len(word)-1) :
        if word[j] != word[j+1] :
            if word[j] in word[j+1:] :
                res = False
                break
    if res :
        cnt += 1
print(cnt)
