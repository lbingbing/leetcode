class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int left_cnt = 0;
        for(int v : data){
            if(left_cnt==0){
                if((v&0x80)==0) ;
                else if((v&0xe0)==0xc0) left_cnt = 1;
                else if((v&0xf0)==0xe0) left_cnt = 2;
                else if((v&0xf8)==0xf0) left_cnt = 3;
                else return 0;
            }else{
                if((v&0xc0)!=0x80) return 0;
                --left_cnt;
            }
        }
        return left_cnt==0;
    }
};
