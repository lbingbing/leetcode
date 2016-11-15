class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0;
        for(int i=0,j=height.size()-1;i<j;){
            int l = height[i];
            int r = height[j];
            res = max(res,(j-i)*min(l,r));
            if(l<=r) while(i<j&&height[i]<=l) ++i;
            if(l>=r) while(i<j&&height[j]<=r) --j;
        }
        return res;
    }
};
