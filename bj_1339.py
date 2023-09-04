N = int(input())
word = []
word_dict = {}
num_list = []
for i in range(N) :
    w = input()
    word.append(w)

for i in range(N) :
    for j in range(len(word[i])) :
        if word[i][j] in word_dict :
            word_dict[word[i][j]] += 10  ** (len(word[i])-j-1)
        else :
            word_dict[word[i][j]] = 10 ** (len(word[i])-j-1)


for i in word_dict.values() :
    num_list.append(i)
num_list.sort(reverse=True)
sum = 0
pows = 9
for i in num_list :
    sum += pows * i
    pows -= 1
print(sum)

