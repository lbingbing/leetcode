class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int pos = min(int(nums.size()),k+1);
        set<int> s(nums.begin(),nums.begin()+pos);
        if(s.size()<pos) return 1;
        for(int i=pos;i<nums.size();++i){
            // erase before insert for cases where nums[i-k-1]==nums[i]
            s.erase(nums[i-k-1]);
            s.insert(nums[i]);
            if(s.size()<k+1) return 1;
        }
        return 0;
    }
};
