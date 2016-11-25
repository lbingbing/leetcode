class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        heap = [None]*k # heap[i]: nums index
        ptr = [None]*len(nums) # ptr[i]: heap index of nums[i]
        for i in range(0,len(nums)):
            if i>=k:
                # remove nums[i-k] from heap
                heap[ptr[i-k]] = heap[k-1]
                ptr[heap[k-1]] = ptr[i-k]
                self.heapify(nums,heap,k,ptr,ptr[i-k])
            # add nums[i] to heap
            j = min(i,k-1)
            heap[j] = i
            ptr[i] = j
            self.heapify(nums,heap,j+1,ptr,j)
            if i>=k-1:
                res.append(nums[heap[0]])
        return res

    def heapify(self, nums, heap, size, ptr, i):
        while i>0:
            p = (i-1)//2
            if nums[heap[i]]>nums[heap[p]]:
                heap[i],heap[p] = heap[p],heap[i]
                ptr[heap[i]],ptr[heap[p]] = ptr[heap[p]],ptr[heap[i]]
                i = p
            else:
                break
        while i<size:
            c1 = i*2+1
            c2 = i*2+2
            if c1<size and nums[heap[i]]<nums[heap[c1]] and (c2>=size or nums[heap[c1]]>=nums[heap[c2]]):
                heap[i],heap[c1] = heap[c1],heap[i]
                ptr[heap[i]],ptr[heap[c1]] = ptr[heap[c1]],ptr[heap[i]]
                i = c1
            elif c2<size and nums[heap[i]]<nums[heap[c2]] and nums[heap[c2]]>=nums[heap[c1]]:
                heap[i],heap[c2] = heap[c2],heap[i]
                ptr[heap[i]],ptr[heap[c2]] = ptr[heap[c2]],ptr[heap[i]]
                i = c2
            else:
                break
