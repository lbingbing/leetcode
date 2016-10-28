class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if(nums.size()){
            vector<int> nums1(nums.begin(),nums.end()-1);
            vector<vector<int>> res = subsets(nums1);
            vector<vector<int>> res1(res);
            for(auto &e : res1){
                e.push_back(nums[nums.size()-1]);
            }
            copy(make_move_iterator(res1.begin()),make_move_iterator(res1.end()),back_inserter(res));
            return res;
        }else{
            return {{}};
        }
    }
};
