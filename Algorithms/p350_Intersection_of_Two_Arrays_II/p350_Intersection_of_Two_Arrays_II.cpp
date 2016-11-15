class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        vector<int> res;
        int len1 = nums1.size();
        int len2 = nums2.size();
        for(int i1=0,i2=0;i1<len1&i2<len2;){
            if(nums1[i1]<nums2[i2]){
                i1++;
            }else if(nums1[i1]>nums2[i2]){
                i2++;
            }else{
                res.push_back(nums1[i1]);
                i1++;
                i2++;
            }
        }
        return res;
    }
};
