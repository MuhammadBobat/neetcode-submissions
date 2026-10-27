class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        row_size = len(matrix)
        col_size = len(matrix[0])
        r = row_size * col_size - 1

        while l <= r:
            mid = (l+r) // 2
            row = mid // col_size
            col = mid % col_size 
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                l = mid + 1

        return False