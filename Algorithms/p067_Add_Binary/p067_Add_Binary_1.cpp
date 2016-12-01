class Solution {
public:
    string addBinary(string a, string b) {
        if(a.empty()) a = "0";
        if(b.empty()) b = "0";
        string res;
        int i = a.size()-1;
        int j = b.size()-1;
        int c = 0;
        while(i>=0||j>=0){
            int op1 = i>=0 ? a[i]-'0' : 0;
            int op2 = j>=0 ? b[j]-'0' : 0;
            int out = op1+op2+c;
            res += out&0x1 ? '1' : '0';
            c = out>=2 ? 1 : 0;
            if(i>=0) --i;
            if(j>=0) --j;
        }
        if(c>0) res += '1';
        reverse(res.begin(),res.end());
        return res;
    }
};
