class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int len = nums.size();
        int zs;
        for(zs=0;zs<len;zs++){
            if(nums[zs]==0){
                break;
            }
        }
        for(int i=zs+1;i<len;i++){
            if(nums[i]!=0){
                int tmp = nums[zs];
                nums[zs] = nums[i];
                nums[i] = tmp;
                zs++;
            }
        }
    }
};
