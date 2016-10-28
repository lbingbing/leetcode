class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        return findPeakElementHelper(nums,0,nums.size());
    }
    int findPeakElementHelper(vector<int>& nums, int l, int r) {
        int mid = (l+r)/2;
        if((mid==0 || nums[mid]>nums[mid-1]) && (mid==nums.size()-1 || nums[mid]>nums[mid+1])){
            return mid;
        }else if((mid==0 || nums[mid]>nums[mid-1]) && (mid<nums.size()-1 && nums[mid]<nums[mid+1])){
            return findPeakElementHelper(nums,mid+1,r);
        }else{
            return findPeakElementHelper(nums,l,mid);
        }
    }
};
