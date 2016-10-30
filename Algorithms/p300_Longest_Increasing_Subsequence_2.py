class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        table = [None]*n
        table[0] = nums[0]
        size = 1
        for i in range(1,n):
            """
            l = 0
            r = size
            while l<r:
                mid = (l+r)//2
                if table[mid]<nums[i]:
                    l = mid+1
                else:
                    r = mid
            table[l] = nums[i]
            if l==size:
                size += 1
            """
            j = bisect.bisect_left(table,nums[i],0,size)
            table[j] = nums[i]
            if j==size:
                size += 1
        return size
