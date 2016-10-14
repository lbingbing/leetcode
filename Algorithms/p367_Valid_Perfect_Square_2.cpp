class Solution {
public:
    bool isPerfectSquare(int num) {
        for(int l=1,r=num+1;l<r;){
            int mid = (l+r)/2;
            int q = num/mid;
            if(mid<q)      l = mid+1;
            else if(mid>q) r = mid;
            else           return mid*mid==num;
        }
        return 0;
    }
};
