// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int l = 1;
        int r = n+1;
        while(1){
            int mid = l+(r-l)/2;
            int cmp = guess(mid);
            if(cmp<0){
                r = mid;
            }else if(cmp>0){
                l = mid+1;
            }else{
                return mid;
            }
        }
        return 0; // dummy return
    }
};
