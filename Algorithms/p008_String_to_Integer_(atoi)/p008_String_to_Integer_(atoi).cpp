class Solution {
public:
    int myAtoi(string str) {
        int i = 0;
        while(i<str.size()&&str[i]==' ') ++i;
        if(i<str.size()){
            long long res = 0;
            bool positive = 1;
            if(str[i]=='+'){
                ++i;
            }else if(str[i]=='-'){
                positive = 0;
                ++i;
            }
            while(i<str.size()){
                if(str[i]>='0'&&str[i]<='9'){
                    res = res*10+(str[i]-'0');
                    if(res>numeric_limits<int>::max()){
                        return positive ? numeric_limits<int>::max() : numeric_limits<int>::min();
                    }
                    ++i;
                }else{
                    break;
                }
            }
            return positive ? res : -res;
        }
        return 0;
    }
};
