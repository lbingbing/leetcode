class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        return permuteUniqueHelper(nums);
    }
    vector<vector<int>> permuteUniqueHelper(vector<int>& nums) {
        if(nums.empty()) return {{}};
        vector<vector<int>> res;
        for(int i=0;i<nums.size();++i){
            if(i>0&&nums[i]==nums[i-1]) continue;
            vector<int> nums1(nums.begin(),nums.begin()+i);
            nums1.insert(nums1.end(),nums.begin()+i+1,nums.end());
            vector<vector<int>> res1 = permuteUniqueHelper(nums1);
            for(auto &e : res1){
                e.insert(e.begin(),nums[i]);
            }
            res.insert(res.end(),make_move_iterator(res1.begin()),make_move_iterator(res1.end()));
        }
        return res;
    }
};
