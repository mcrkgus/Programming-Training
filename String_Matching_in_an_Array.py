class Solution:
    def stringMatching(self, words: List[str]) -> List[str] :

        words.sort(key=lambda x : len(x))

        ans = []


        def kmp(all_string, pattern) :
            p = len(pattern)
            s = len(all_string)
            table = [0 for _ in range(p)]
            i = 0
            for j in range(1, p) :
                while i > 0 and pattern[i] != pattern[j] :
                    i = table[i-1]
                
                if pattern[i] == pattern[j] :
                    i += 1
                    table[j] = i
            
            result = []
            i = 0
            for j in range(s) :
                while i > 0 and pattern[i] != all_string[j] :
                    i = table[i-1]
                    
                if pattern[i] == all_string[j] :
                    i += 1
                    if i == p :
                        result.append(j-i+1)
                        i = table[i-1]
                        
            return result

        for i in range(len(words)-1) :
            for j in range(i+1, len(words)) :
                res = kmp(words[j], words[i])
                if len(res) != 0 :
                    ans.append(words[i])
        ans = list(set(ans))
        return ans
