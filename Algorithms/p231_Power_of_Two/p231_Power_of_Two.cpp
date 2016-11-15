class Solution {
public:
    bool isPowerOfTwo(int n) {
        while(n>1){
            if(n>>1<<1!=n){
                return 0;
            }
            n >>= 1;
        }
        return n>0;
    }
};
