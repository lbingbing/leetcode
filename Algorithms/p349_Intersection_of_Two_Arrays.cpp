class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        int i1 = 0;
        int i2 = 0;
        int len1 = nums1.size();
        int len2 = nums2.size();
        vector<int> res;
        while(i1<len1 && i2<len2){
            int n1 = nums1[i1];
            int n2 = nums2[i2];
            if(n1<n2){
                i1++;
            }else if(n1>n2){
                i2++;
            }else{
                if(res.empty() || res.back()!=n1){
                    res.push_back(n1);
                }
                i1++;
                i2++;
            }
        }
        return res;
    }
};
