class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        q = len(nums)-1
        while p<q:
            mid = (p+q)//2
            cnt = 0
            for v in nums:
                if v<=mid:
                    cnt += 1
            if cnt<=mid:
                p = mid+1
            else:
                q = mid
        return p
