class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        state = []
        self.combinationSumStep(res,state,candidates,0,target)
        return res
        
    def combinationSumStep(self, res, state, candidates, ptr, target):
        if target==0:
            res.append(state[:])
        elif ptr<len(candidates):
            max_num = target//candidates[ptr]
            target = target%candidates[ptr]
            state += [candidates[ptr]]*max_num
            while max_num>=0:
                self.combinationSumStep(res,state,candidates,ptr+1,target)
                target += candidates[ptr]
                if max_num>0:
                    del state[-1]
                max_num -= 1
