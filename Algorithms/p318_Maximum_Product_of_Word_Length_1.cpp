class Solution {
public:
    int maxProduct(vector<string>& words) {
        int len = words.size();
        vector<int> words_len(len);
        for(int i=0;i<len;i++){
            words_len[i] = words[i].size();
            sort(words[i].begin(),words[i].end());
        }
        int res = 0;
        for(int i1=0;i1<len-1;i1++){
            for(int i2=i1+1;i2<len;i2++){
                int len1 = words_len[i1];
                int len2 = words_len[i2];
                int v = len1*len2;
                if(v>res){
                    int k1,k2;
                    for(k1=0,k2=0;k1<len1&&k2<len2;){
                        char c1 = words[i1][k1];
                        char c2 = words[i2][k2];
                        if(c1<c2){
                            k1++;
                        }else if(c1>c2){
                            k2++;
                        }else{
                            break;
                        }
                    }
                    if(k1==len1 || k2==len2){
                        res = v;
                    }
                }
            }
        }
        return res;
    }
};
