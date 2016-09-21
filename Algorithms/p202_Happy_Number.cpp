class Solution {
public:
    bool isHappy(int n) {
        bool table[810] = {};
        while(1){
            int m = 0;
            while(n){
                int d = n%10;
                m += d*d;
                n /= 10;
            }
            n = m;
            if(n==1){
                return 1;
            }
            if(table[n]){
                return 0;
            }else{
                table[n] = 1;
            }
        }
        return 0; // dummy
    }
};
