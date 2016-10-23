class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int j = nums.size()-1;
        while(1){
            while(i<=j&&nums[i]!=val) ++i;
            while(i<=j&&nums[j]==val) --j;
            if(i>=j) break;
            swap(nums[i],nums[j]);
        }
        return i;
    }
};
