class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int a = 0;
        int b = 0;
        for(int v : nums){
            int b_n = (b&~v)|(a&v);
            int a_n = (a&~v)|(~b&~a&v);
            b = b_n;
            a = a_n;
        }
        return a;
    }
};
