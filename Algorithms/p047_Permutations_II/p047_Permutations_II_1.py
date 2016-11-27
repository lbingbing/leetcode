class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        cur = []
        visited = [False]*len(nums)
        self.permuteUniqueHelper(res,cur,nums,visited)
        return res

    def permuteUniqueHelper(self, res, cur, nums, visited):
        for i in range(len(nums)):
            if visited[i] or i>0 and nums[i]==nums[i-1] and visited[i-1]==False:
                continue
            cur.append(nums[i])
            visited[i] = True
            if len(cur)==len(nums):
                res.append(cur[:])
            else:
                self.permuteUniqueHelper(res,cur,nums,visited);
            cur.pop()
            visited[i] = False
