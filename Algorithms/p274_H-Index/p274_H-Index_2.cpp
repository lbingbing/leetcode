class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        vector<int> cnt(n+1,0);
        for(int v : citations){
            if(v>n) ++cnt[n];
            else ++cnt[v];
        }
        for(int i=n;i>=0;--i){
            if(cnt[i]>=i) return i;
            cnt[i-1] += cnt[i];
        }
        return 0; // dummy return
    }
};
