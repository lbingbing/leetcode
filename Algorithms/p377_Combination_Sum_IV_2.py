class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        table = [0]*(target+1)
        table[0] = 1
        for i in range(1,target+1):
            for v in nums:
                if i>=v:
                    table[i] += table[i-v]
        return table[target]
