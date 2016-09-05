class Solution {
public:
    int maxProduct(vector<string>& words) {
        int len = words.size();
        vector<vector<int>> cnt(len,vector<int>(256,0));
        for(int i=0;i<len;i++){
            int distinct_char_num = 0;
            for(char c : words[i]){
                if(!cnt[i][c]){
                    cnt[i][c] = 1;
                    distinct_char_num++;
                    if(distinct_char_num==256){
                        break;
                    }
                }
            }
        }
        int res = 0;
        for(int i1=0;i1<len-1;i1++){
            for(int i2=i1+1;i2<len;i2++){
                int v = words[i1].size()*words[i2].size();
                if(v>res){
                    int j;
                    for(j=0;j<256;j++){
                        if(cnt[i1][j] && cnt[i2][j]){
                            break;
                        }
                    }
                    if(j==256){
                        res = v;
                    }
                }
            }
        }
        return res;
    }
};
