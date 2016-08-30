class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int cur_v = nums[0];
        int cur_cnt = 1;
        int max_v = cur_v;
        int max_cnt = cur_cnt;
        int len = nums.size();
        for(int i=1;i<len;i++){
            if(nums[i]==cur_v){
                cur_cnt++;
            }else{
                if(cur_cnt>max_cnt){
                    max_v = cur_v;
                    max_cnt = cur_cnt;
                }
                cur_v = nums[i];
                cur_cnt = 1;
            }
        }
        if(cur_cnt>max_cnt){
            max_v = cur_v;
            max_cnt = cur_cnt;
        }
        return max_v;
    }
};
