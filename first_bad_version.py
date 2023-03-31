class Solution:
    def firstBadVersion(self, n: int) -> int:
        # edge cases:
        if n == 1:
            if isBadVersion(1):
                return 1
            else:
                return -1
        elif n == 2:
            if isBadVersion(1):
                return 1
            elif isBadVersion(2):
                return 2
            else:
                return -1
        
        # binary search:
        left = 1
        right = n
        while left <= right:
            middle = (left + right) // 2
            
            # check middle if 1st bad version:
            if isBadVersion(middle) and not isBadVersion(middle-1):
                return middle
            # else if in right half:
            elif not isBadVersion(middle):
                left = middle + 1
                right = right
            # else in left half:
            else:
                left = left
                right = middle - 1