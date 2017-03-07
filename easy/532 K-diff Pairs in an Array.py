class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        index = 0
        observed = []
        if k < 0:
            return 0
        for i,v in enumerate(nums):
            try:
                nums[i] = None
                next =nums.index(v+k)

            except:
                nums[i] = v
            else:
                nums[i] = v
                if (v, nums[index]) not in observed:
                    count+=1
                    observed.append((v,nums[index]))
                    observed.append((nums[index],v))


        return count

sol = Solution()
print(sol.findPairs([1, 3, 1, 5, 4], 0))