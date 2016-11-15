class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int res = 1;
        for(int i=0,f=1;i<n && i<10;i++){
            res += 9*f;
            f *= 9-i;
        }
        return res;
    }
};
