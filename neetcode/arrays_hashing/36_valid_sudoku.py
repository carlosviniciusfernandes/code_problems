# https://leetcode.com/problems/valid-sudoku/

from typing import List

#! Solution1 worked on first try and beated 95% :)

class Solution1:
    def validateArr(self, arr: List[str])-> None | Exception:
        clearedArr = [item for item in arr if item != '.']
        arrSet = set(clearedArr)
        if len(arrSet) != len(clearedArr):
            raise Exception('not valid')

    def getSubBoxArr(self, index: int,  board: List[List[str]]) -> List[str]:
        rowIndex = index // 3
        colIndex = index % 3

        arr = []
        for i in range(3):
            for j in range(3):
                arr.append(board[rowIndex*3 + i][colIndex*3 +j])
        return arr

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        try:
            for i in range(0, 9):
                row = board[i]
                self.validateArr(row)

            tboard = [*zip(*board)]
            for i in range(0, 9):
                col = tboard[i]
                self.validateArr(col)

            for i in range(0, 9):
                box = self.getSubBoxArr(i, board)
                self.validateArr(box)

            return True
        except Exception as e:
            if str(e) == 'not valid':
                return False
            raise e

from collections import defaultdict

class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True