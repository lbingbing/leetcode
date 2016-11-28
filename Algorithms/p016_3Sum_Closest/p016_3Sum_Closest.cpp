class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        
        int max2 = nums[n-2]+nums[n-1];
        int low = 0;
        while(low<=n-3&&nums[low]+max2<target) ++low;
        if(low>0) --low;
        
        int min2 = nums[0]+nums[1];
        int high = n-1;
        while(high>=2&&nums[high]+min2>target) --high;
        if(high<n-1) ++high;
        
        int res;
        int diff = numeric_limits<int>::max();
        for(int i=low;i<=high-2;++i){
            int l = i+1;
            int r = high;
            while(l<r){
                int target1 = nums[i]+nums[l]+nums[r];
                int diff1 = abs(target1-target);
                if(diff1<diff){
                    res = target1;
                    diff = diff1;
                }
                if(target1<target)      ++l;
                else if(target1>target) --r;
                else                    return target;
            }
        }
        return res;
    }
};
