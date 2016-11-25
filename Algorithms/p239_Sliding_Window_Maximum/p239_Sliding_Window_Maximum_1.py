class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dq = collections.deque()
        for i in range(0,len(nums)):
            if dq and i-dq[0]==k:
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res
