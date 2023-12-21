N, score, P = map(int, input().split())
res = 0
my_rank = 1

score_list = list(map(int, input().split()))
score_list.sort(reverse=True)


# 이미 랭킹 리스트가 꽉 차 있으면서 최저 점수와 점수가 같거나 작을 경우
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
