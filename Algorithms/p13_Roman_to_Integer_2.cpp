class Solution {
public:
    int romanToInt(string s) {
        int len = s.size();
        vector<int> l(len);
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
        for(int i=1;i<len;i++){
            if(l[i]>l[i-1]){
                l[i-1] = -l[i-1];
            }
        }
        return accumulate(l.begin(),l.end(),0);
    }
};
