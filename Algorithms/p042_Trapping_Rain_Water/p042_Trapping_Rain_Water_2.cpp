class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int res = 0;
        int l = 0;
        int r = n-1;
        int l_max = 0;
        int r_max = 0;
        while(l<=r){
            if(l_max<r_max){
                if(height[l]>=l_max) l_max = height[l];
                else res += l_max-height[l];
                ++l;
            }else{
                if(height[r]>=r_max) r_max = height[r];
                else res += r_max-height[r];
                --r;
            }
        }
        return res;
    }
};
