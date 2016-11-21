class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> nums1_1(nums1);
        for(int i=0,j1=0,j2=0;i<m+n;++i){
            if(j1<m&&(j2==n||nums1_1[j1]<nums2[j2])){
                nums1[i] = nums1_1[j1++];
            }else{
                nums1[i] = nums2[j2++];
            }
        }
    }
};
