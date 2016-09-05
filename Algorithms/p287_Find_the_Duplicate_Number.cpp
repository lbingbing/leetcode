class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int p = 1;
        int q = nums.size()-1;
        while(p<q){
            int mid = (p+q)/2;
            int cnt = 0;
            for(int v : nums){
                if(v<=mid){
                    cnt++;
                }
            }
            if(cnt<=mid){
                p = mid+1;
            }else{
                q = mid;
            }
        }
        return p;
    }
};
