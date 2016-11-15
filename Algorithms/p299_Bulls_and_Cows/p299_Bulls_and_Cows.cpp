class Solution {
public:
    string getHint(string secret, string guess) {
        vector<int> secret_cnt(10,0);
        vector<int> guess_cnt(10,0);
        int a_cnt = 0;
        int b_cnt = 0;
        for(int i=0;i<secret.size();++i){
            if(secret[i]==guess[i]){
                ++a_cnt;
            }else{
                ++secret_cnt[secret[i]-'0'];
                ++guess_cnt[guess[i]-'0'];
            }
        }
        for(int i=0;i<10;++i){
            b_cnt += min(secret_cnt[i],guess_cnt[i]);
        }
        return to_string(a_cnt)+"A"+to_string(b_cnt)+"B";
    }
};
