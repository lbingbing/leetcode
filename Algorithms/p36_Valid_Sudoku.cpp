class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> cnt(10);
        for(int i=0;i<9;++i){
            for(int &v : cnt){
                v = 0;
            }
            for(int j=0;j<9;++j){
                if(board[i][j]=='.') continue;
                if(!(board[i][j]>='0'&&board[i][j]<='9')) return 0;
                if(cnt[board[i][j]-'0']) return 0;
                cnt[board[i][j]-'0'] = 1;
            }
        }
        for(int j=0;j<9;++j){
            for(int &v : cnt){
                v = 0;
            }
            for(int i=0;i<9;++i){
                if(board[i][j]=='.') continue;
                if(cnt[board[i][j]-'0']) return 0;
                cnt[board[i][j]-'0'] = 1;
            }
        }
        for(int u=0;u<9;u+=3){
            for(int l=0;l<9;l+=3){
                for(int &v : cnt){
                    v = 0;
                }
                for(int i=u;i<u+3;++i){
                    for(int j=l;j<l+3;++j){
                        if(board[i][j]=='.') continue;
                        if(!(board[i][j]>='0'&&board[i][j]<='9')) return 0;
                        if(cnt[board[i][j]-'0']) return 0;
                        cnt[board[i][j]-'0'] = 1;
                    }
                }
            }
        }
        return 1;
    }
};
