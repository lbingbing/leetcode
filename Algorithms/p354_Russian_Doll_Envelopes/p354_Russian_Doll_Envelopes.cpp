class Solution {
public:
    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        sort(envelopes.begin(),envelopes.end(),[](pair<int,int>& e1, pair<int,int>& e2){ return e1.first<e2.first||e1.first==e2.first&&e1.second>e2.second; });
        // min_h[i]: min h of i-length sequence's last envelope so far
        vector<int> min_h(envelopes.size()+1,0);
        int max_len = 0;
        for(auto &e : envelopes){
            int j = lower_bound(min_h.begin(),min_h.begin()+(max_len+1),e.second)-min_h.begin();
            min_h[j] = e.second;
            if(j>max_len) max_len = j;
        }
        return max_len;
    }
};
