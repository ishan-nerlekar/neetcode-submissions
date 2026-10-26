class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictrow = defaultdict(set)
        dictcol = defaultdict(set)
        dictsquare = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==".":
                    continue
                else:
                    if(board[i][j] in dictrow[i] or board[i][j] in dictcol[j] or board[i][j] in dictsquare[(i//3,j//3)]):
                        return False
                    dictrow[i].add(board[i][j])
                    dictcol[j].add(board[i][j])
                    dictsquare[(i//3,j//3)].add(board[i][j])
        return True