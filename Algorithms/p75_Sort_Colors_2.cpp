class Solution {
public:
    void sortColors(vector<int>& nums) {
        for(int i=0,j0=-1,j1=-1;i<nums.size();++i){
            if(nums[i]==0){
                swap(nums[++j1],nums[i]);
                swap(nums[++j0],nums[j1]);
            }else if(nums[i]==1){
                swap(nums[++j1],nums[i]);
            }
        }
    }
};
