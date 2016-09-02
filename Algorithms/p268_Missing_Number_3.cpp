class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::default_random_engine dre;
        int p1 = 0;
        int p2 = nums.size()-1;
        // recursive partition
        while(p2-p1>1){
            std::uniform_int_distribution<int> di(p1+1,p2-1);
            int p = di(dre);
            int x = nums[p];
            nums[p] = nums[p2];
            nums[p2] = x;
            int j = p1;
            for(int i=p1;i<p2;i++){
                if(nums[i]<x){
                    if(i!=j){
                        int tmp = nums[i];
                        nums[i] = nums[j];
                        nums[j] = tmp;
                    }
                    j++;
                }
            }
            if(j<p2){
                nums[p2] = nums[j];
                nums[j] = x;
            }
            if(j<x){
                p2 = j;
            }else{
                p1 = j;
            }
        }
        if(p2<0){
            return 0;
        }
        if(nums[p1]>nums[p2]){
            int tmp = nums[p1];
            nums[p1] = nums[p2];
            nums[p2] = tmp;
        }
        if(p1<nums[p1]){
            return p1;
        }else if(p2<nums[p2]){
            return p2;
        }else{
            return p2+1;
        }
    }
};
