# //https://leetcode.com/problems/summary-ranges/?tab=Description
# Given a sorted integer array without duplicates, return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
  pseudocode
  Things to note: array is sorted. can start with the first element and visit one by one
  util the next integer is not the consecutive integer or its the last element of the array.
  result = []
  index=0
  first = nums[0]
  for first element to last element of nums


 index++
  if index >  last index of nums
  if current == first append first to result and return
  if not append first->current append that to result

  current = nums[index]
if current not equal to first+1
last = previous of current element
if last=first then add just first else add first->last
and first = current
 append first->current to result

Test
[0,1,2,4,5,7]
first = 0
curr = 1
curr =2
curr = 4
last = 2
add to result 0->2
first = 4
cur=5
cur = 7
last =5
append 4->5
first = 7
add 7
"""



class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) < 1:
            return result
        first = nums[0]
        if len(nums) == 1:
            result.append(str(nums[0]))
            return result
        index = 1
        while(index < len(nums)):
            current = nums[index]
            previous = nums[index-1]
            if current != previous+1:
                last = previous
                self.append_result(first,last,result)
                first = current
            if index == len(nums)-1:
                self.append_result(first,nums[index],result)
                return result
            index = index+1


        return result



    def append_result(self, first, last, result):
        if last == first:
            result.append(str(first))

        else:
            result.append(str(first)+ '->' + str(last))
        return result


sol = Solution().summaryRanges([-1])
print(sol)