class Solution {
public:
    int lengthLongestPath(string input) {
        stack<int> base_dirs;
        int cur_len = 0;
        int cur_pos = 0;
        int max_path_len = 0;
        while(1){
            int tab_num = 0;
            while(cur_pos<input.size()&&input[cur_pos]=='\t'){
                ++tab_num;
                ++cur_pos;
            }
            if(cur_pos==input.size()) break;
            for(int i=base_dirs.size()-tab_num;i>0;--i){
                cur_len -= base_dirs.top();
                base_dirs.pop();
            }
            bool is_file = 0;
            int cur_pos1 = cur_pos;
            while(cur_pos1<input.size()&&input[cur_pos1]!='\n'){
                if(input[cur_pos1]=='.') is_file = 1;
                ++cur_pos1;
            }
            cur_len += cur_pos1-cur_pos;
            if(is_file){
                if(cur_len>max_path_len) max_path_len = cur_len;
            }
            ++cur_len; // add '/'
            base_dirs.push(cur_pos1-cur_pos+1); // add '/'
            if(cur_pos1==input.size()) break;
            cur_pos = cur_pos1+1; // skip '\n'
        }
        return max_path_len;
    }
};
