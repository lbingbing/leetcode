class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = binarySearch(nums,target,1);
        if(start>=nums.size() || nums[start]>target) return {-1,-1};
        int end = binarySearch(nums,target,0);
        return {start,end-1};
    }
    int binarySearch(vector<int>& nums, int target, bool lower) {
        int l = 0;
        int r = nums.size();
        while(l<r){
            int mid = l+(r-l)/2;
            if(nums[mid]<target){
                l = mid+1;
            }else if(nums[mid]>target){
                r = mid;
            }else{
                if(lower) r = mid;
                else      l = mid+1;
            }
        }
        return l;
    }
};
