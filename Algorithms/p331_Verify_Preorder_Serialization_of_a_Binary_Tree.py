class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return False
        cnt = 1
        pos = 0
        while pos!=-1 and cnt>0:
            pos = preorder.find(',',pos+1)
            if (pos!=-1 and preorder[pos-1]=='#') or (pos==-1 and preorder[-1]=='#'):
                cnt -= 1
            else:
                cnt += 1
        return pos==-1 and cnt==0
