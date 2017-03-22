"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [1, 0, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        slow=0
        fast=1
        while fast < len(nums):
            if nums[slow] != 0:
                slow+=1
                fast+=1
                continue
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                nums[fast]=0
                fast+=1
                slow+=1
            else:
                fast+=1
        # print(nums)

print(Solution().moveZeroes( [0]))