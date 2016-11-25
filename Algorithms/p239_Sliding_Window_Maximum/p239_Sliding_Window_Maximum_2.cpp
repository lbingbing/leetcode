class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        vector<int> heap(k); // heap[i]: nums index
        vector<int> ptr(nums.size()); // ptr[i]: heap index of nums[i]
        for(int i=0;i<nums.size();++i){
            if(i>=k){
                // remove nums[i-k] from heap
                heap[ptr[i-k]] = heap[k-1];
                ptr[heap[k-1]] = ptr[i-k];
                heapify(nums,heap,k,ptr,ptr[i-k]);
            }
            // add nums[i] to heap
            int j = min(i,k-1);
            heap[j] = i;
            ptr[i] = j;
            heapify(nums,heap,j+1,ptr,j);
            if(i>=k-1) res.push_back(nums[heap[0]]);
        }
        return res;
    }
    void heapify(vector<int>& nums, vector<int>& heap, int size, vector<int>& ptr, int i) {
        while(i>0){
            int p = (i-1)/2;
            if(nums[heap[i]]>nums[heap[p]]){
                swap(heap[i],heap[p]);
                swap(ptr[heap[i]],ptr[heap[p]]);
                i = p;
            }else{
                break;
            }
        }
        while(i<size){
            int c1 = i*2+1;
            int c2 = i*2+2;
            if(c1<size&&nums[heap[i]]<nums[heap[c1]]&&(c2>=size||nums[heap[c1]]>=nums[heap[c2]])){
                swap(heap[i],heap[c1]);
                swap(ptr[heap[i]],ptr[heap[c1]]);
                i = c1;
            }else if(c2<size&&nums[heap[i]]<nums[heap[c2]]&&nums[heap[c2]]>=nums[heap[c1]]){
                swap(heap[i],heap[c2]);
                swap(ptr[heap[i]],ptr[heap[c2]]);
                i = c2;
            }else{
                break;
            }
        }
    }
};
