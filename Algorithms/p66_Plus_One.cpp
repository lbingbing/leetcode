class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> res(digits.rbegin(),digits.rend());
        int i = 0;
        for(i=0;i<res.size();++i){
            ++res[i];
            if(res[i]==10) res[i] = 0;
            else break;
        }
        if(i==res.size()) res.push_back(1);
        reverse(res.begin(),res.end());
        return res;
    }
};
