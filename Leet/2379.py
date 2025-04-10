class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if 'B'*k in blocks: return 0

        n=len(blocks)
        if n==k: return len([1 for x in blocks if x == 'W'])

        ops = [0 for i in range(n-k+1)]

        for i in range(n-k+1):
            cl = blocks[i:i+k]  # checklist 

            for x in cl:
                if x == 'W':
                    ops[i]+=1   # list of number of operations

        return min(ops)