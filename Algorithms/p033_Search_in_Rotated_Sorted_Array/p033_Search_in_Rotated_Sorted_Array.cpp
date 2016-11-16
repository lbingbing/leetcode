class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.empty()) return -1;
        int n = nums.size();
        int l = 0;
        int r = n;
        int left_most = nums[l];
        while(l<r){
            int mid = l+(r-l)/2;
            if(nums[mid]<left_most){
                r = mid;
            }else{
                l = mid+1;
            }
        }
        int p = l; // start of 2nd part, or n when no rotation
        if(target>=nums[0]&&target<=nums[p-1]){
            l = 0;
            r = p;
        }else if(p<n&&target>=nums[p]&&target<=nums[n-1]){
            l = p;
            r = n;
        }else{
            return -1;
        }
        while(l<r){
            int mid = l+(r-l)/2;
            if(target<nums[mid]){
                r = mid;
            }else if(target>nums[mid]){
                l = mid+1;
            }else{
                return mid;
            }
        }
        return -1;
    }
};
