"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
"""


class Solution(object):
    def findComplement(self,num):
        """
        :type num: int
        :rtype: int
        """
        complement_num = []
        while (num):
            bit = 1 & num
            num = num >> 1
            bit_inverse = 0 if bit else 1
            complement_num.append(bit_inverse)
        # reverse it because we are storing LSB first.
        complement_num.reverse()
        complement_num = ''.join(map(str, complement_num))
        return int(complement_num, 2)


def tes():
    sol = Solution()
    print(sol.findComplement(1))


tes()
