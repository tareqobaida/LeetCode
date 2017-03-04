"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for bit in nums:
            if bit:
                count += 1
                if count > result:
                    result = count
            else:
                count = 0
        return result

def test():
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,0,0,1,1,0,1,1,1,1]))

test()