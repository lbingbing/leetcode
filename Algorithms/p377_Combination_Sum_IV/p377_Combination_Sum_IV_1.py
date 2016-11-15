class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        table = [None]*(target+1)
        return self.getCombinationSum4(table,nums,target)
        
    def getCombinationSum4(self, table, nums, target):
        if table[target]==None:
            table[target] = 0
            for v in nums:
                if target>v:
                    table[target] += self.getCombinationSum4(table,nums,target-v)
                elif target==v:
                    table[target] += 1
        return table[target]
