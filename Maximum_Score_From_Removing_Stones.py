class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        #a=b=c일 때 홀수 -> 1->4->7->...
        #a=b=c일 때 짝수 -> 3->6->9->...
        d = max(a, b, c)
        sum1 = int((a+b+c) / 2)
        sum2 = (a+b+c) - d

        if sum1 < sum2 :
            return sum1
        return sum2
