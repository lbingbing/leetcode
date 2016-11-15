class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums)>1:
            for i in range(0,len(nums)):
                nums1 = nums[:]
                del nums1[i:i+1]
                res1 = self.permute(nums1)
                for e in res1:
                    e.insert(0,nums[i])
                res += res1
        elif len(nums)==1:
            res.append([nums[0]]);
        else:
            res.append([])
        return res
