import random

class Solution1(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findPeakElementHelper(nums,0,len(nums))

    def findPeakElementHelper(self, nums, l, r):
        mid = (l+r)//2
        if (mid==0 or nums[mid]>nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
            return mid
        elif (mid==0 or nums[mid]>nums[mid-1]) and (mid<len(nums)-1 and nums[mid]<nums[mid+1]):
            return self.findPeakElementHelper(nums,mid+1,r)
        else:
            return self.findPeakElementHelper(nums,l,mid)

class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)
        while True:
            mid = (l+r)//2
            if (mid==0 or nums[mid]>nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            elif (mid==0 or nums[mid]>nums[mid-1]) and (mid<len(nums)-1 and nums[mid]<nums[mid+1]):
                l = mid+1
            else:
                r = mid
        return -1 # dummy return

m = 100
n = 30

s1 = Solution1()
s2 = Solution2()

def check(l,res):
    return (res==0 or l[res]>l[res-1]) and (res==len(l)-1 or l[res]>l[res+1])

for m1 in range(0,m):
    l = []
    n1 = random.randint(1,n)
    for i in range(0,n1):
        while True:
            v = random.randint(0,n1)
            if i==0 or v!=l[-1]:
                break
        l.append(v)
    print(str(l).replace(' ',''))
    res = s1.findPeakElement(l)
    if not check(l,res):
        print(str(l).replace(' ',''))
        print('error')
    res = s2.findPeakElement(l)
    if not check(l,res):
        print(str(l).replace(' ',''))
        print('error')
