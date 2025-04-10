class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        
        rn = len(grid)
        n = rn**2
        collect = [] #list of all numbers in grid


        for i in range(rn):
            ls = grid[i]
            for j in range(rn):
                collect.append(ls[j])

        collect.sort()
        print("collect:",collect)


        dl = [collect[i-1]-i for i in range(1,n+1)] #difference list
        print("dl:",dl)
        ans = [] 
        ones = [i for i,x in enumerate(dl) if x!=0] #list of index where dl is not 0
        print("ones:",ones)
        f = ones[0]; l = ones[-1] #first and last index where diff not 0 

        ans = [collect[l], collect[f]-1] 
        if -1 in dl:
            ans[0], ans[1] = ans[1]+1, ans[0]+1

        return ans

print(Solution().findMissingAndRepeatedValues([[1,2,3],[3,4,5],[6,7,9]])) 