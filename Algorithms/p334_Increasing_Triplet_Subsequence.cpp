class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int v1 = std::numeric_limits<int>::max();
        int v2 = std::numeric_limits<int>::max();
        for(int v : nums){
            if(v<=v1)      v1 = v;
            else if(v<=v2) v2 = v;
            else           return 1;
        }
        return 0;
    }
};
