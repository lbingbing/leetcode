class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            cnt = set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if not (ord(board[i][j])>=ord('1') and ord(board[i][j])<=ord('9')):
                    return False
                if board[i][j] in cnt:
                    return False
                cnt.add(board[i][j])
        for j in range(9):
            cnt = set()
            for i in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in cnt:
                    return False
                cnt.add(board[i][j])
        for u in (0,3,6):
            for l in (0,3,6):
                cnt = set()
                for i in range(u,u+3):
                    for j in range(l,l+3):
                        if board[i][j]=='.':
                            continue
                        if board[i][j] in cnt:
                            return False
                        cnt.add(board[i][j])
        return True
