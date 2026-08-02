class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        line_h = [False] * 10
        line_v = [False] * 10
        grid_1 = [False] * 10
        grid_2 = [False] * 10
        grid_3 = [False] * 10

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if line_h[int(board[i][j])] == True:
                        return False
                    line_h[int(board[i][j])] = True
                if board[j][i] != ".":
                    if line_v[int(board[j][i])] == True:
                        return False
                    line_v[int(board[j][i])] = True
            del line_h
            del line_v
            line_h = [False] * 10
            line_v = [False] * 10

        x = 0
        y = 1
        z = 2

        for i in range(9):
            if (i > 0 and i % 3 == 0):
                del grid_1
                del grid_2
                del grid_3
                grid_1 = [False] * 10
                grid_2 = [False] * 10
                grid_3 = [False] * 10

            if board[x][i] != ".":
                if grid_1[int(board[x][i])] == True:
                    return False
                grid_1[int(board[x][i])] = True
            if board[y][i] != ".":
                if grid_1[int(board[y][i])] == True:
                    return False
                grid_1[int(board[y][i])] = True
            if board[z][i] != ".":
                if grid_1[int(board[z][i])] == True:
                    return False
                grid_1[int(board[z][i])] = True
            
            if board[x+3][i] != ".":
                if grid_2[int(board[x+3][i])] == True:
                    return False
                grid_2[int(board[x+3][i])] = True
            if board[y+3][i] != ".":
                if grid_2[int(board[y+3][i])] == True:
                    return False
                grid_2[int(board[y+3][i])] = True
            if board[z+3][i] != ".":
                if grid_2[int(board[z+3][i])] == True:
                    return False
                grid_2[int(board[z+3][i])] = True

            if board[x+6][i] != ".":
                if grid_3[int(board[x+6][i])] == True:
                    return False
                grid_3[int(board[x+6][i])] = True
            if board[y+6][i] != ".":
                if grid_3[int(board[y+6][i])] == True:
                    return False
                grid_3[int(board[y+6][i])] = True
            if board[z+6][i] != ".":
                if grid_3[int(board[z+6][i])] == True:
                    return False
                grid_3[int(board[z+6][i])] = True

        return True