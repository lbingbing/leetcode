class Solution {
public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        sort(people.begin(),people.end(),[](pair<int,int>& a, pair<int,int>& b){ return a.first<b.first || a.first==b.first&&a.second>b.second; });
        int n = people.size();
        vector<pair<int, int>> res(n);
        vector<int> used(n,0);
        for(int i=0;i<n;++i){
            int cnt = people[i].second;
            int j = 0;
            while(1){
                if(used[j]==0){
                    --cnt;
                    if(cnt<0) break;
                }
                ++j;
            }
            res[j] = people[i];
            used[j] = 1;
        }
        return res;
    }
};
