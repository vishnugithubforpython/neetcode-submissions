class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            hash=[]
            for col in range(9):
                num=board[row][col]

                if num == ".":
                    continue

                if num in hash:
                    return False
                else:
                    hash.append(num)

        for col in range(9):
            hash1=[]
            for row in range(9):
                num=board[row][col]
                if num == ".":
                    continue
                if num in hash1:
                    return False
                else:
                    hash1.append(num)

        for box in range(9):
            hash2=[]
            start_row=box//3*3
            start_col=box%3 *3
            for row in range(start_row,start_row+3):
                for col in range(start_col, start_col+3):
                    num=board[row][col]
                    if num == ".":
                        continue
                    if num in hash2:
                        return False
                    else:
                        hash2.append(num)

        return True


        