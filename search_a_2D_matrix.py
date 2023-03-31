class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get dimensions:
        m = len(matrix)
        n = len(matrix[0])

        # binary search over rows:
        low = 0
        high = m-1
        found_row = None
        while low <= high:
            middle = (low + high) // 2

            # if in row:
            if target >= matrix[middle][0] and target <= matrix[middle][n-1]:
                found_row = middle
                break
            # else if in "left" half:
            elif target < matrix[middle][0]:
                low = low
                high = middle - 1
            # else if in  "right" half:
            else:
                low = middle + 1
                high = high
        # if not in any row:
        if found_row is None:
            return False
        
        # binary search over columns (in a single row):
        low = 0
        high = n-1
        while low <= high:
            middle = (low + high) // 2

            # if target found:
            if target == matrix[found_row][middle]:
                return True
            # else if in left half:
            if target < matrix[found_row][middle]:
                low = low
                high = middle - 1
            # else if in right half:
            else:
                low = middle + 1
                high = high
        # if target not found:
        return False