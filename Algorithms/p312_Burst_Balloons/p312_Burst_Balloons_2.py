class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        nums.insert(0,1)
        nums.append(1)
        coin = [[-1]*(nums_len+2) for i in range(0,nums_len+2)]
        for i in range(1,nums_len+2):
            coin[i][i-1] = 0
        return self.getMaxCoins(nums,coin,1,nums_len);
        
    def getMaxCoins(self, nums, coin, i, j):
        if coin[i][j]==-1:
            for k in range(i,j+1):
                coin[i][j] = max(coin[i][j], nums[i-1]*nums[k]*nums[j+1]+self.getMaxCoins(nums,coin,i,k-1)+self.getMaxCoins(nums,coin,k+1,j))
        return coin[i][j]
