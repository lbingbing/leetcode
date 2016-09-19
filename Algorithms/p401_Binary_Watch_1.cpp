class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        if(num<0 || num>10){
            return {};
        }
        
        vector<vector<vector<int>>> values(7,vector<vector<int>>(7)); // table[width][ones]={values}
        for(auto &e : values){
            e[0].push_back(0);
        }
        for(int i=1;i<values.size();++i){
            values[i][i].push_back((1<<i)-1);
        }
        for(int i=2;i<values.size();++i){
            for(int j=1;j<i;++j){
                values[i][j].insert(values[i][j].end(),values[i-1][j].begin(),values[i-1][j].end());
                vector<int> tmp = values[i-1][j-1];
                for_each(tmp.begin(),tmp.end(),[i](int &v){ v += 1<<(i-1); });
                values[i][j].insert(values[i][j].end(),tmp.begin(),tmp.end());
            }
        }
        vector<string> res;
        for(int i=max(0,num-6);i<=min(4,num);++i){
            for(int h : values[4][i]){
                if(h<12){
                    for(int m : values[6][num-i]){
                        if(m<60){
                            if(m<10){
                                res.push_back(to_string(h)+":0"+to_string(m));
                            }else{
                                res.push_back(to_string(h)+":"+to_string(m));
                            }
                        }
                    }
                }
            }
        }
        return res;
    }
};
