class Solution {
public:
    int rob(vector<int>& nums) {
        int s0 = 0; // no robbing
        int s1 = 0; // robbing
        for(int v : nums){
            int tmp = s0;
            s0 = max(s0,s1);
            s1 = tmp+v;
        }
        return max(s0,s1);
    }
};
