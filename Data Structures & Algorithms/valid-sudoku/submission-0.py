class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictrow=defaultdict(set)
        dictcol=defaultdict(set)
        dictsquares=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c]=='.'):
                    continue
                if(board[r][c] in dictrow[r] or board[r][c] in dictcol[c] or board[r][c] in dictsquares[(r//3,c//3)]):
                    return False
                dictrow[r].add(board[r][c])
                dictcol[c].add(board[r][c])
                dictsquares[(r//3,c//3)].add(board[r][c])
        return True