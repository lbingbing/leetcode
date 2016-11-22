class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        int add = 0;
        long long int max_n = 0;
        int i = 0;
        while(max_n<n){
            if(i==nums.size()||nums[i]>max_n+1){
                max_n += max_n+1;
                ++add;
            }else{
                max_n += nums[i++];
            }
        }
        return add;
    }
};
