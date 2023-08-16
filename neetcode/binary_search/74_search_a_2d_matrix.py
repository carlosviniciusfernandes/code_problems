# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        lower_row = 0
        upper_row = len(matrix) - 1

        while lower_row <= upper_row:
            row = (lower_row + upper_row) // 2
            if target > matrix[row][-1]: #* row last element
                lower_row += 1
            elif target < matrix[row][0]: #* row first element
                upper_row -= 1
            else:
                break

        left_col = 0
        right_col = len(matrix[0]) - 1

        while left_col <= right_col:
            col = (left_col + right_col) // 2
            if target < matrix[row][col]:
                right_col -= 1
            elif target > matrix[row][col]:
                left_col += 1
            else:
                return True

        return False
