class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(),citations.end(),greater<int>());
        int cnt = 0;
        for(int v : citations){
            ++cnt;
            if(v<cnt) --cnt;
            if(v<=cnt) break;
        }
        return cnt;
    }
};
