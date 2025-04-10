class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        l = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                l.append(
                    words[i] in words[j] and
                words[j].index(words[i])==0 and
                words[j][::-1].index(words[i][::-1])==0
                )

        return sum(l)