class Solution:
    def maxScore(self, s: str) -> int:
        ones = [i for i in range(1,len(s)) if s[i] == '1' and s[i-1]=='0'] #index of ones 

        scores = []
        
        for i in range(len(ones)):
            s1 = map(int,s[:ones[i]]); s2 = map(int,s[ones[i]:])
            s1 = list(s1); s2 = list(s2)
            scores.append(len(s1)-sum(s1)+sum(s2))
            print(s1,s2)
            print(i, scores)
            print()
        print()
        return max(scores,default=0)

print(Solution.maxScore(Solution,"011101")) #5