class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        n = len(nums)
        l = 0
        r = n
        while True:
            x = nums[r-1]
            j = l-1
            for i in range(l,r-1):
                if nums[i]<x:
                    j += 1
                    nums[i],nums[j] = nums[j],nums[i]
            j += 1
            nums[j],nums[r-1] = nums[r-1],nums[j]
            if j<n-k:
                l = j+1
            elif j>n-k:
                r = j
            else:
                res = nums[j]
                break
        return res
