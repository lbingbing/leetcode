class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        random_shuffle(nums.begin(),nums.end());
        int n = nums.size();
        int l = 0;
        int r = n;
        int res;
        while(1){
            int x = nums[r-1];
            int j = l-1;
            for(int i=l;i<r;++i){
                if(nums[i]<x) swap(nums[i],nums[++j]);
            }
            swap(nums[++j],nums[r-1]);
            if(j<n-k){
                l = j+1;
            }else if(j>n-k){
                r = j;
            }else{
                res = nums[j];
                break;
            }
        }
        return res;
    }
};
