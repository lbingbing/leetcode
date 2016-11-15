class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s1(nums1.begin(),nums1.end());
        set<int> s2(nums2.begin(),nums2.end());
        set<int>* p_s;
        set<int>* p_l;
        vector<int> res;
        if(s1.size()>s2.size()){
            p_l = &s1;
            p_s = &s2;
        }else{
            p_l = &s2;
            p_s = &s1;
        }
        for(int v : *p_s){
            if(p_l->find(v)!=p_l->end()){
                res.push_back(v);
            }
        }
        return res;
    }
};
