class Solution {
public:
    int integerBreak(int n) {
        if(n==2){
            return 1;
        }else if(n==3){
            return 2;
        }
        int res = 1;
        for(int i=0;i<n/3-1;i++){
            res *= 3;
        }
        if(n%3==0){
            return res*3;
        }else if(n%3==1){
            return res*4;
        }else{
            return res*6;
        }
    }
};
