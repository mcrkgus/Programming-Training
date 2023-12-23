N, score, P = map(int, input().split())
res = 0
my_rank = 1

score_list = list(map(int, input().split()))
score_list.sort(reverse=True)


if (P == len(score_list)) :
    if (score_list[-1] <= score) :
        res = -1
else :
    for i in score_list :
        if score >= i :
            res = my_rank
        else :
            my_rank += 1

print("result", res)
