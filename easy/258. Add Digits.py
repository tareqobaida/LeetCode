"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        if len(num_list) == 1: return num
        num_list_numbers = [int(item) for item in num_list]
        return self.addDigits(sum(num_list_numbers))

print(Solution().addDigits(38))