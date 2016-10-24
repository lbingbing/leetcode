class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        old_state = [None]*n
        for i in range(0,m):
            for j in range(0,n):
                cnt = 0
                if i>0 and j>0:     cnt += old_state[j-1]
                if i>0:             cnt += old_state[j]
                if i>0 and j<n-1:   cnt += old_state[j+1]
                if j>0:             cnt += old_left_state
                if j<n-1:           cnt += board[i][j+1]
                if i<m-1 and j>0:   cnt += board[i+1][j-1]
                if i<m-1:           cnt += board[i+1][j]
                if i<m-1 and j<n-1: cnt += board[i+1][j+1]
                if j>0: old_state[j-1] = old_left_state
                old_left_state = board[i][j]
                if board[i][j]==1 and (cnt<2 or cnt>3): board[i][j] = 0
                elif board[i][j]==0 and cnt==3:         board[i][j] = 1
                if j==n-1: old_state[j] = old_left_state
