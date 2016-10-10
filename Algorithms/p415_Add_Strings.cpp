class Solution {
public:
    string addStrings(string num1, string num2) {
        int l = max(num1.size(),num2.size());
        string res;
        res.reserve(l);
        int j1 = num1.size()-1;
        int j2 = num2.size()-1;
        int carry = 0;
        for(int i=0;i<l;++i){
            int din1 = j1>=0 ? num1[j1]-'0' : 0;
            int din2 = j2>=0 ? num2[j2]-'0' : 0;
            int dout = din1+din2+carry;
            carry = dout>=10 ? 1 : 0;
            dout = dout>=10 ? dout-10 : dout;
            res += '0'+dout;
            if(j1>=0) --j1;
            if(j2>=0) --j2;
        }
        if(carry==1){
            res += '1';
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
