"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
a^b^a = 0
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        for i in range(1, len(nums)):
            a^=nums[i]
        return a

sol = Solution()
print(sol.singleNumber([1,2,1,3,3]))