class Solution {
public:
    Solution(vector<int> nums) {
        this->nums = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return nums;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> res(nums);
        int len = res.size();
        for(int i=0;i<len-1;i++){
            std::uniform_int_distribution<int> di(i,len-1);
            int j = di(dre);
            int tmp = res[i];
            res[i] = res[j];
            res[j] = tmp;
        }
        return res;
    }
    
private:
    vector<int> nums;
    std::default_random_engine dre;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
