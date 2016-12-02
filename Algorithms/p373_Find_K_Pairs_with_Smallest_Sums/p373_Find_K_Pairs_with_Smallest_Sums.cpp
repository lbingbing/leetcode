class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        if(nums1.empty()||nums2.empty()||k==0) return {};
        int m = nums1.size();
        int n = nums2.size();
        auto cmp = [&](pair<int,int>& a, pair<int,int>& b){ return nums1[a.first]+nums2[a.second]>nums1[b.first]+nums2[b.second]; };
        priority_queue<pair<int,int>,vector<pair<int,int>>,decltype(cmp)> heap(cmp);
        if(m<=n){
            for(int i=0;i<m&&i<k;++i){
                heap.emplace(i,0);
            }
        }else{
            for(int j=0;j<n&&j<k;++j){
                heap.emplace(0,j);
            }
        }
        vector<pair<int,int>> res;
        while(k>0&&!heap.empty()){
            auto e = heap.top();
            heap.pop();
            res.emplace_back(nums1[e.first],nums2[e.second]);
            if(m<=n){
                if(e.second<n-1) heap.emplace(e.first,e.second+1);
            }else{
                if(e.first<m-1) heap.emplace(e.first+1,e.second);
            }
            --k;
        }
        return res;
    }
};
