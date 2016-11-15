class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.empty()) return 0;
        int n = nums.size();
        vector<int> table(n);
        table[0] = nums[0];
        int size = 1;
        for(int i=1;i<n;++i){
            /*
            int l = 0;
            int r = size;
            while(l<r){
                int mid = (l+r)/2;
                if(table[mid]<nums[i]){
                    l = mid+1;
                }else{
                    r = mid;
                }
            }
            table[l] = nums[i];
            if(l==size) ++size;
            */
            int j = lower_bound(table.begin(),table.begin()+size,nums[i])-table.begin();
            table[j] = nums[i];
            if(j==size) ++size;
        }
        return size;
    }
};
