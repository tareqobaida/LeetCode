"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
"""



class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        from collections import deque
        carry = 0
        sum = 0
        q = deque()
        while(a or b or carry):
            rmb_a = a & 1
            rmb_b = b & 1
            sum = carry ^ rmb_a ^ rmb_b
            q.appendleft(sum)
            carry = rmb_a & rmb_b | rmb_a & carry | rmb_b & carry
            a= a>>1
            b = b>> 1
        num = ''.join([str(item) for item in q])
        return int(num,2)

sol = Solution()
print(sol.getSum(-1,-1))