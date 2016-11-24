class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<vector<int>> res;
        vector<int> cur;
        dfs(res,cur,candidates,target,0);
        return res;
    }
    void dfs(vector<vector<int>>& res, vector<int>& cur, vector<int>& candidates, int target, int i) {
        for(int j=i,last=-1;j<candidates.size();++j){
            if(candidates[j]>target) break;
            if(candidates[j]==last) continue;
            cur.push_back(candidates[j]);
            if(candidates[j]<target){
                dfs(res,cur,candidates,target-candidates[j],j+1);
            }else if(candidates[j]==target){
                res.push_back(cur);
            }
            cur.pop_back();
            last = candidates[j];
        }
    }
};
