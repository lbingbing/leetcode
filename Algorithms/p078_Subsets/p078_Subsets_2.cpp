class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int w = nums.size();
        int n = 0x1<<w;
        vector<int> cnt(w,0);
        vector<vector<int>> res(n);
        for(int i=0;i<n;++i){
            for(int j=0;j<w;++j){
                if(cnt[j]){
                    res[i].push_back(nums[j]);
                }
            }
            for(int j=0;j<w;++j){
                if(cnt[j]==0){
                    cnt[j] = 1;
                    break;
                }else{
                    cnt[j] = 0;
                }
            }
        }
        return res;
    }
};
