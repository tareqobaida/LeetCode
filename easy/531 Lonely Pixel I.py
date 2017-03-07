"""
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input:
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
"""

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        resultdict = {}
        result = []
        rows = []
        cols = []
        for k, v in enumerate(picture):
            for k2, v2 in enumerate(picture):
                if v2 == 'B':
                    result.append((k,k2))
                    rows.append(k)
                    cols.append(k2)
                    if k in resultdict:
                        del resultdict[k]
                    else:
                        resultdict[k] = k2



        nextdict = {}
        for k, v in resultdict:
            if v in nextdict:
                del nextdict[v]
            else:
                nextdict[v] = k

        return len(nextdict)



sol = Solution()
print(sol.findLonelyPixel([['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]
))