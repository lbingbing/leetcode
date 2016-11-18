class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(nums.empty()) return 0;
        int pos = min(int(nums.size()),k+1);
        set<int> s{nums[0]};
        for(int i=1;i<nums.size();++i){
            // erase before insert for cases where nums[i-k-1]==nums[i]
            if(i>=pos) s.erase(nums[i-k-1]);
            auto res = s.insert(nums[i]);
            if(!res.second&&t>=0){
                return 1;
            }else{
                if(res.first!=s.begin()&&static_cast<long long int>(*res.first)-static_cast<long long int>(*prev(res.first))<=static_cast<long long int>(t)) return 1;
                if(next(res.first)!=s.end()&&static_cast<long long int>(*next(res.first))-static_cast<long long int>(*res.first)<=static_cast<long long int>(t)) return 1;
            }
        }
        return 0;
    }
};
