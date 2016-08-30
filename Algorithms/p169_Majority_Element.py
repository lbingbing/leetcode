class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        cur_v = nums[0]
        cur_cnt = 1
        max_v = cur_v
        max_cnt = cur_cnt
        for i in range(1,len(nums)):
            if nums[i]==cur_v:
                cur_cnt += 1
            else:
                if cur_cnt>max_cnt:
                    max_v = cur_v
                    max_cnt = cur_cnt
                cur_v = nums[i]
                cur_cnt = 1
        if cur_cnt>max_cnt:
            max_v = cur_v
            max_cnt = cur_cnt
        return max_v
