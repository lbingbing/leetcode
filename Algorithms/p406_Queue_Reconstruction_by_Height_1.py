class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        res = [None]*n
        used = [False]*n
        for h,k in sorted(people,key=lambda (h,k):(h,-k)):
            cnt = k
            j = 0
            while True:
                if not used[j]:
                    cnt -= 1
                    if cnt<0:
                        break
                j += 1
            res[j] = [h,k]
            used[j] = True
        return res
