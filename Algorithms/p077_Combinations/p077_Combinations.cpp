class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        return combineHelper(n,k,1);
    }
    vector<vector<int>> combineHelper(int n, int k, int start) {
        if(start>n||k==0) return {{}};
        vector<vector<int>> res = combineHelper(n,k-1,start+1);
        for(auto &e : res){
            e.insert(e.begin(),start);
        }
        if(n-start>=k){
            vector<vector<int>> res1 = combineHelper(n,k,start+1);
            res.insert(res.end(),res1.begin(),res1.end());
        }
        return res;
    }
};
