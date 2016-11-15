class Solution {
public:
    bool isPowerOfThree(int n) {
        while(n>=3){
            if(n/3*3!=n){
                return 0;
            }
            n /= 3;
        }
        return n==1;
    }
};
