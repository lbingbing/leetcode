class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        if(nums.empty()) return {{}};
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        vector<int> cur;
        vector<int> visited(nums.size(),0);
        permuteUniqueHelper(res,cur,nums,visited);
        return res;
    }
    void permuteUniqueHelper(vector<vector<int>>& res, vector<int>& cur, vector<int>& nums, vector<int>& visited) {
        for(int i=0;i<nums.size();++i){
            if(visited[i]||i>0&&nums[i]==nums[i-1]&&visited[i-1]==0) continue;
            cur.push_back(nums[i]);
            visited[i] = 1;
            if(cur.size()==nums.size()) res.push_back(cur);
            else permuteUniqueHelper(res,cur,nums,visited);
            cur.pop_back();
            visited[i] = 0;
        }
    }
};
