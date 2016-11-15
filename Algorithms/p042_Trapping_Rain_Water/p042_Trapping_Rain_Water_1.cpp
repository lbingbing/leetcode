class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> l_max(n,0);
        vector<int> r_max(n,0);
        for(int i=1;i<n;++i){
            l_max[i] = max(l_max[i-1],height[i-1]);
        }
        for(int i=n-2;i>=0;--i){
            r_max[i] = max(r_max[i+1],height[i+1]);
        }
        int res = 0;
        for(int i=1;i<n-1;++i){
            res += max(min(l_max[i],r_max[i])-height[i],0);
        }
        return res;
    }
};
