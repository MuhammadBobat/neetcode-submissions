class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        # r represents length of the fully flattened 2D array
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            #// would give how far into the row, % would give the row
            mid = (l+r) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False