class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        if(num<0 || num>10){
            return {};
        }
        
        vector<vector<string>> values1(5);
        for(int i=0;i<12;++i){
            values1[countOnes(i)].push_back(to_string(i));
        }
        vector<vector<string>> values2(7);
        for(int i=0;i<60;++i){
            values2[countOnes(i)].push_back((i<10?"0":"")+to_string(i));
        }
        
        vector<string> res;
        for(int i=max(0,num-6);i<=min(4,num);++i){
            for(const string& h : values1[i]){
                for(const string& m : values2[num-i]){
                    res.push_back(h+":"+m);
                }
            }
        }
        return res;
    }
    int countOnes(int v){
        int num = 0;
        for(int i=0;i<32;++i){
            if(v&0x1){
                ++num;
            }
            v >>= 1;
        }
        return num;
    }
};
