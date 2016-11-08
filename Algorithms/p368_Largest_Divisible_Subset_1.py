class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums.sort()
        # length[i]: max length of set with last(max) value being nums[i]
        # previous[i]: index of nums[i]'s predecessor in optimal solution
        length = [1]*n
        previous = [-1]*n
        max_len = 0
        max_index = -1
        for i in range(n):
            for j in range(i):
                if length[j]>=length[i] and nums[i]%nums[j]==0:
                    length[i] = length[j]+1
                    previous[i] = j
            if length[i]>max_len:
                max_len = length[i]
                max_index = i
        res = []
        while max_index!=-1:
            res.append(nums[max_index])
            max_index = previous[max_index]
        return res
