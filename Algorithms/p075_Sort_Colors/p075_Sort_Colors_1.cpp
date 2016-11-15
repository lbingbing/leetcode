class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> cnt(3,0);
        for(int v : nums){
            ++cnt[v];
        }
        for(int i=0,j=0;j<3;++j){
            for(;cnt[j];--cnt[j]){
                nums[i++] = j;
            }
        }
    }
};
