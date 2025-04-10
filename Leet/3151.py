class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        nums1 = [x for x in nums[::2]]
        nums2 = [x for x in nums[1::2]]
        print(nums1,nums2)

        if not((sum(nums1)%2 == 0 and len(nums1)%2 == 0) and (sum(nums2)%2 == 0 and len(nums2)%2 == 0)):
            return False

        return True