class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> state;
        combinationSum3Helper(res,state,k,n,1);
        return res;
    }
    void combinationSum3Helper(vector<vector<int>>& res, vector<int>& state, int k, int n, int start){
        if(k>0){
            for(int i=max(start,n-(20-k)*(k-1)/2);(i*2+k-1)*k/2<=n;++i){
                state.push_back(i);
                combinationSum3Helper(res,state,k-1,n-i,i+1);
                state.pop_back();
            }
        }else{
            res.push_back(state);
        }
    }
};
