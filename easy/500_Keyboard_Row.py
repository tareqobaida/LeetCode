"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        alphabets = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0,
                     'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1,
                     'z': 2, 'x': 2, 'c': 2, 'v': 2, 'b': 2, 'n': 2, 'm': 2}
        if len(alphabets) != 26:
            raise ValueError

        for word in words:
            if not word:
                break
            word_lowercase = word.lower()
            flag = True
            holder = set()
            for letter in word_lowercase:
                holder.add(alphabets[letter])
                if len(holder) > 1:
                    flag = False
                    break
            if flag:
                result.append(word)
        return result


def test():
    sol = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace", 'aaaaa', '']
    print(sol.findWords(words))


test()
