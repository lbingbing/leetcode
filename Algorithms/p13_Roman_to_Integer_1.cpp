class Solution {
public:
    int romanToInt(string s) {
        int len = s.size();
        if(len){
            vector<int> l(len+1);
            for(int i=0;i<len;i++){
                switch(s[i]){
                    case 'I': l[i] = 1; break;
                    case 'V': l[i] = 5; break;
                    case 'X': l[i] = 10; break;
                    case 'L': l[i] = 50; break;
                    case 'C': l[i] = 100; break;
                    case 'D': l[i] = 500; break;
                    case 'M': l[i] = 1000; break;
                    default:  l[i] = 0;
                }
            }
            l[len] = 0;
            int res = 0;
            int inc_start = 0;
            int last_v = l[0];
            for(int i=1;i<=len;i++){
                if(l[i]<=last_v){
                    for(int j=inc_start;j<i-1;j++){
                        res -= l[j];
                    }
                    res += l[i-1];
                    inc_start = i;
                }
                last_v = l[i];
            }
            return res;
        }else{
            return 0;
        }
    }
};
