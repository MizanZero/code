class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l1 = list(s1); l2 = list(s2)
        l1.sort(); l2.sort()
        if l1 != l2: return False
        n = len(s1)
        diff = 0
        i=0

        while i<n:
            if s1[i] != s2[i] : diff+=1
            i+=1

        return False if diff>2 else True