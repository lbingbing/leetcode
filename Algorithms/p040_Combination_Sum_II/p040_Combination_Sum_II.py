class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        cur = []
        self.dfs(res,cur,candidates,target,0)
        return res

    def dfs(self, res, cur, candidates, target, i):
        last = -1
        for j in range(i,len(candidates)):
            if candidates[j]>target:
                break
            if candidates[j]==last:
                continue
            cur.append(candidates[j])
            if candidates[j]<target:
                self.dfs(res,cur,candidates,target-candidates[j],j+1)
            elif candidates[j]==target:
                res.append(cur[:])
            cur.pop()
            last = candidates[j]
