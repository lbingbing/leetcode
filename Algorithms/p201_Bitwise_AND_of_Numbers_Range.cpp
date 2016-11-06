class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int res = 0;
        for(int i=0;i<31;++i){
            int group_size = 0x1<<(i+1);
            int half_group_size = 0x1<<i;
            if(m/group_size==n/group_size&&m%group_size>=half_group_size) res |= 0x1<<i;
        }
        return res;
    }
};
