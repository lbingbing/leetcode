class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> table(target+1,0);
        table[0] = 1;
        for(int i=1;i<=target;++i){
            for(int v : nums){
                if(i>=v){
                    table[i] += table[i-v];
                }
            }
        }
        return table[target];
    }
};
