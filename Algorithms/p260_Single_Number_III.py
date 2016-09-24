class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import functools
        res1_xor_res2 = functools.reduce(operator.xor,nums)
        mask = 0x1
        while res1_xor_res2&mask==0:
            mask <<= 1
        res1 = functools.reduce(operator.xor,filter(lambda x: x&mask,nums))
        res2 = functools.reduce(operator.xor,filter(lambda x: not x&mask,nums))
        return [res1,res2]
