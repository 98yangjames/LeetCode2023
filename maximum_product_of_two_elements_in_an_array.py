class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Approach 1:
        heap = []
        for num in nums:   # O(N log3)
            heapq.heappush(heap, num)   # O(log 2)
            if len(heap) > 2:
                heapq.heappop(heap)   # O(log 3)
        
        # get 2 largest elements:
        second_largest = heapq.heappop(heap)   # O(log 2)
        first_largest = heapq.heappop(heap)   # O(1)

        max_prod = (first_largest-1) * (second_largest-1)
        
        return max_prod

        
        # Approach 2:
        """
        two_largest = heapq.nlargest(2, nums)   # O(N log2)
        max_prod = (two_largest[0]-1) * (two_largest[1]-1)
        
        return max_prod
        """

        
        # Approach 3:
        """
        # build max heap:
        nums = [-num for num in nums]   # O(N)
        heapq.heapify(nums)   # O(N)
        
        # get 2 largest elements:
        first_largest = -1 * heapq.heappop(nums)   # O(logN)
        second_largest = -1 * heapq.heappop(nums)   # O(logN)

        max_prod = (first_largest-1) * (second_largest-1)

        return max_prod
        """