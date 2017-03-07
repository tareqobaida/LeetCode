"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Input: "USA"
Output: True
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def is_all_upper(word):
            word_list = [x.upper() == x for x in word]
            return all(word_list)

        def is_all_lower(word):
            word_list = [x.lower() == x for x in word]
            return all(word_list)

        if is_all_upper(word[0]):
            return is_all_upper(word[1:]) or is_all_lower(word[1:])
        else:
            return is_all_lower(word)




sol = Solution()
print(sol.detectCapitalUse('USA'))
print(sol.detectCapitalUse('Usa'))
print(sol.detectCapitalUse('usA'))
print(sol.detectCapitalUse('usa'))
