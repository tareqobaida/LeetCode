"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        self.result = s.split()
        length = len(s)
        end_point = False
        left_over = ''

        for start in range(0, length, k * 2):
            if end_point:
                break
            if (length - start < 2 * k) and (length - start > k):
                end = start + k
                left_over = s[end+1:]
                end_point = True
            elif length - start < k:
                end = len(s) - 1
            else:
                end = start + k
            while (start < end):
                self.result[start] = s[end]
                self.result[end] = s[start]
                start += 1
                end -= 1

        return ''.join(self.result) + left_over


sol = Solution()
print(sol.reverseStr("abcdefg", 2))
