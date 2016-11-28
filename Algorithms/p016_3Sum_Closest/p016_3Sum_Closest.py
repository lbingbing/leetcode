class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        
        max2 = nums[n-2]+nums[n-1]
        low = 0
        while low<=n-3 and nums[low]+max2<target:
            low += 1
        if low>0:
            low -= 1
        
        min2 = nums[0]+nums[1]
        high = n-1
        while high>=2 and nums[high]+min2>target:
            high -= 1
        if high<n-1:
            high += 1
        
        res = nums[low]+nums[low+1]+nums[low+2]
        diff = abs(res-target)
        for i in range(low,high-1):
            l = i+1
            r = high
            while l<r:
                target1 = nums[i]+nums[l]+nums[r]
                diff1 = abs(target1-target)
                if diff1<diff:
                    res = target1
                    diff = diff1
                if target1<target:
                    l += 1
                elif target1>target:
                    r -= 1
                else:
                    return target
        return res
