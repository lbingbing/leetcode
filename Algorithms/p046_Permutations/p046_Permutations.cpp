class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size()>1){
            for(int i=0;i<nums.size();++i){
                vector<int> nums1(nums);
                nums1.erase(nums1.begin()+i);
                vector<vector<int>> res1 = permute(nums1);
                for(auto &e : res1){
                    e.insert(e.begin(),nums[i]);
                }
                res.insert(res.end(),res1.begin(),res1.end());
            }
        }else if(nums.size()==1){
            res.push_back(vector<int>(1,nums[0]));
        }else{
            res.push_back(vector<int>());
        }
        return res;
    }
};
