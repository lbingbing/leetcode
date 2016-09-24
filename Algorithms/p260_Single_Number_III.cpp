class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int res1_xor_res2 = accumulate(nums.begin(),nums.end(),0,[](int a, int b){ return a^b; });
        int mask = 0x1;
        while(!(res1_xor_res2&mask)){
            mask <<= 1;
        }
        int res1 = 0;
        int res2 = 0;
        for(int v : nums){
            if(v&mask){
                res1 ^= v;
            }else{
                res2 ^= v;
            }
        }
        return {res1,res2};
    }
};
