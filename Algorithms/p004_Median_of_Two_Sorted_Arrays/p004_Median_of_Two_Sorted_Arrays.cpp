class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()<nums2.size()) swap(nums1,nums2);
        int n1 = nums1.size();
        int n2 = nums2.size();
        int k = (n1+n2+1)/2;
        bool double_median = ((n1+n2)%2==0);
        int l1 = 0;
        int r1 = n1;
        int l2 = 0;
        int r2 = n2;
        while(l1<r1){
            int mid = (l1+r1)/2;
            int pos = lower_bound(nums2.begin()+l2,nums2.begin()+r2,nums1[mid])-nums2.begin();
            int k1 = mid+pos+1;
            if(k1<k){
                l1 = mid+1;
                l2 = pos;
            }else if(k1>k){
                r1 = mid;
                r2 = pos;
            }else{
                double median = nums1[mid];
                if(double_median){
                    double median2;
                    if(mid+1>=n1)    median2 = nums2[pos];
                    else if(pos>=n2) median2 = nums1[mid+1];
                    else             median2 = min(nums1[mid+1],nums2[pos]);
                    return (median+median2)/2;
                }
                return median;
            }
        }
        double median = nums2[k-l1-1];
        if(double_median){
            double median2;
            if(l1>=n1)        median2 = nums2[k-l1];
            else if(k-l1>=n2) median2 = nums1[l1];
            else              median2 = min(nums1[l1],nums2[k-l1]);
            return (median+median2)/2;
        }
        return median;
    }
};
