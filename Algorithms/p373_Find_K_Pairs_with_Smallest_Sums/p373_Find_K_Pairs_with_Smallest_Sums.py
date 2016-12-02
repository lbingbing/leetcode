class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k==0:
            return []
        m = len(nums1)
        n = len(nums2)
        l = []
        if m<=n:
            for i in range(min(m,k)):
                heapq.heappush(l,(nums1[i]+nums2[0],i,0))
        else:
            for j in range(min(n,k)):
                heapq.heappush(l,(nums1[0]+nums2[j],0,j))
        res = []
        while k>0 and l:
            e = l[0]
            res.append([nums1[e[1]],nums2[e[2]]])
            if m<=n:
                if e[2]<n-1:
                    heapq.heappushpop(l,(nums1[e[1]]+nums2[e[2]+1],e[1],e[2]+1))
                else:
                    heapq.heappop(l)
            else:
                if e[1]<m-1:
                    heapq.heappushpop(l,(nums1[e[1]+1]+nums2[e[2]],e[1]+1,e[2]))
                else:
                    heapq.heappop(l)
            k -= 1
        return res
