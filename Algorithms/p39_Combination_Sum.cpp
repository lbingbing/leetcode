class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> state;
        combinationSumStep(res,state,candidates,0,target);
        return res;
    }
    void combinationSumStep(vector<vector<int>>& res, vector<int>& state, vector<int>& candidates, int ptr, int target){
        if(target==0){
            res.push_back(state);
        }else if(ptr<candidates.size()){
            int max_num = target/candidates[ptr];
            target = target%candidates[ptr];
            state.insert(state.end(),max_num,candidates[ptr]);
            for(;max_num>=0;--max_num){
                combinationSumStep(res,state,candidates,ptr+1,target);
                target += candidates[ptr];
                if(max_num>0){
                    state.pop_back();
                }
            }
        }
    }
};
