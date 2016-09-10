class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        nums.insert(0,1)
        nums.append(1)
        coin = [[0]*(nums_len+2) for i in range(0,nums_len+2)]
        for l in range(0,nums_len):
            for i in range(1,nums_len-l+1):
                j = i+l
                for k in range(i,j+1):
                    coin[i][j] = max(coin[i][j], nums[i-1]*nums[k]*nums[j+1]+coin[i][k-1]+coin[k+1][j])
        return coin[1][nums_len]
