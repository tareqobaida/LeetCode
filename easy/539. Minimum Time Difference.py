"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
"""
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        result = []
        timePoints.sort()
        timePoints.append(timePoints[0])

        for t in range(len(timePoints)-1):
            t1= [int(x) for x in timePoints[t].split(":")]
            t2= [int(x) for x in timePoints[t+1].split(":")]
            r1 = abs((t1[0]*60 + t1[1]) - (t2[0]*60+t2[1]))
            result.append(min(r1, 24*60-r1))
        return min(result)



sol = Solution()
print(sol.findMinDifference( ["01:01","02:01"]))