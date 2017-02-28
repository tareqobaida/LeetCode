"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
https://leetcode.com/problems/next-greater-element-i/?tab=Description
"""
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        for k,v in enumerate(findNums):
            try:
             index = nums.index(v)
            except ValueError:
                findNums[k] = -1
            else:
                findNums[k] = -1
                for i in range(index+1, len(nums)):
                    if nums[i] > v:
                        findNums[k] = nums[i]
                        break
        return findNums

def test():
    sol = Solution()
    findnums = [2,4]
    nums =  [1,2,3,4]
    print(sol.nextGreaterElement(findnums,nums))

test()