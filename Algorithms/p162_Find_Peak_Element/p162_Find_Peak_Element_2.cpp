class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0;
        int r = nums.size();
        while(1){
            int mid = (l+r)/2;
            if((mid==0 || nums[mid]>nums[mid-1]) && (mid==nums.size()-1 || nums[mid]>nums[mid+1])){
                return mid;
            }else if((mid==0 || nums[mid]>nums[mid-1]) && (mid<nums.size()-1 && nums[mid]<nums[mid+1])){
                l = mid+1;
            }else{
                r = mid;
            }
        }
        return -1; // dummy return
    }
};
