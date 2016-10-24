class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        if(board.size()==0) return;
        int m = board.size();
        int n = board[0].size();
        vector<int> old_state(n);
        int old_left_state;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                int cnt = 0;
                if(i>0&&j>0)     cnt += old_state[j-1];
                if(i>0)          cnt += old_state[j];
                if(i>0&&j<n-1)   cnt += old_state[j+1];
                if(j>0)          cnt += old_left_state;
                if(j<n-1)        cnt += board[i][j+1];
                if(i<m-1&&j>0)   cnt += board[i+1][j-1];
                if(i<m-1)        cnt += board[i+1][j];
                if(i<m-1&&j<n-1) cnt += board[i+1][j+1];
                if(j>0) old_state[j-1] = old_left_state;
                old_left_state = board[i][j];
                if(board[i][j]==1&&(cnt<2||cnt>3)) board[i][j] = 0;
                else if(board[i][j]==0&&cnt==3)    board[i][j] = 1;
                if(j==n-1) old_state[j] = old_left_state;
            }
        }
    }
};
