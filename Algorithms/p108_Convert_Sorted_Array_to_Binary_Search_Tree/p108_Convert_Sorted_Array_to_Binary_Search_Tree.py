# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTStep(nums,0,len(nums)-1)
        
    def sortedArrayToBSTStep(self, nums, i, j):
        if i<=j:
            mid = (i+j)//2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBSTStep(nums,i,mid-1);
            root.right = self.sortedArrayToBSTStep(nums,mid+1,j);
            return root
        else:
            return None
