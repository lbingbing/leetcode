class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> nums1(nums.size());
        for(int i=0;i<nums1.size();++i){
            nums1[i] = make_pair(nums[i],i);
        }
        sort(nums1.begin(),nums1.end(),[](pair<int,int>& e1, pair<int,int>& e2){ return e1.first<e2.first; });
        int l = 0;
        int r = nums1.size()-1;
        while(l<r){
            int sum1 = nums1[l].first+nums1[r].first;
            if(sum1<target){
                ++l;
            }else if(sum1>target){
                --r;
            }else{
                return {min(nums1[l].second,nums1[r].second),max(nums1[l].second,nums1[r].second)};
            }
        }
        return {}; // dummy return
    }
};
