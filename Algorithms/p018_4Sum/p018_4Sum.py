class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l = j+1
                r = n-1
                target1 = target-nums[i]-nums[j]
                while l<r:
                    if nums[l]+nums[r]<target1:
                        l += 1
                    elif nums[l]+nums[r]>target1:
                        r -= 1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l<r and nums[l]==nums[l-1]:
                            l += 1
                        while l<r and nums[r]==nums[r+1]:
                            r -= 1
        return res
