class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return 0;
        int l_mask = 1;
        int h_mask = 1;
        int x1 = x;
        while(x1>=10){
            x1 /= 10;
            h_mask *= 10;
        }
        while(l_mask<h_mask){
            if((x/l_mask)%10!=(x/h_mask)%10) return 0;
            l_mask *= 10;
            h_mask /= 10;
        }
        return 1;
    }
};
