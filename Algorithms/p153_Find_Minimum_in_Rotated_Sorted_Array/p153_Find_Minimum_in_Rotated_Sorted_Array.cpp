class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0;
        int r = nums.size()-1;
        while(l<r){
            int mid = (l+r)/2;
            int x = nums[mid];
            if(nums[l]>x){
                r = mid;
            }else if(x>nums[r]){
                l = mid+1;
            }else{
                break;
            }
        }
        return nums[l];
    }
};
