class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l = 0
            r = len(row) - 1
            while l <= r:
                mid = (l+r) // 2
                if row[mid] == target:
                    return True
                elif target > row[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False