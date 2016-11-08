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
            for j in range(i+1,n):
                if length[i]>=length[j] and nums[j]%nums[i]==0:
                    length[j] = length[i]+1
                    previous[j] = i
            if length[i]>max_len:
                max_len = length[i]
                max_index = i
        res = []
        while max_index!=-1:
            res.append(nums[max_index])
            max_index = previous[max_index]
        return res
