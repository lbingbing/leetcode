class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        // length[i]: max length of set with last(max) value being nums[i]
        // previous[i]: index of nums[i]'s predecessor in optimal solution
        vector<int> length(n,1);
        vector<int> previous(n,-1);
        int max_len = 0;
        int max_index = -1;
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                if(length[i]>=length[j]&&nums[j]%nums[i]==0){
                    length[j] = length[i]+1;
                    previous[j] = i;
                }
            }
            if(length[i]>max_len){
                max_len = length[i];
                max_index = i;
            }
        }
        vector<int> res;
        while(max_index!=-1){
            res.push_back(nums[max_index]);
            max_index = previous[max_index];
        }
        return res;
    }
};
