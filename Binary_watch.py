class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        #8,2,1 #4,2,1 #8,2 #8,1 #4,2 #4,1 #2,1 
        res = []
        for h in range(12) :
            for m in range(60) :
                bin_num = bin(h) + bin(m)
                if bin_num.count('1') == turnedOn :
                    res.append("%d:%02d" % (h, m))
        return res
