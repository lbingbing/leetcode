class Solution {
public:
    string toHex(int num) {
        if(num!=0){
            unsigned int n = num;
            string res;
            while(n){
                int d = n&0xf;
                if(d>=0 && d<10){
                    res.insert(res.begin(),'0'+d);
                }else{
                    res.insert(res.begin(),'a'+d-10);
                }
                n >>= 4;
            }
            return res;
        }else{
            return "0";
        }
    }
};
