class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # build min heap:
        heapq.heapify(nums)     # O(N)

        # pop off elements one-by-one:
        nums_sort = []
        while len(nums) != 0:     # O(N logN)
            nums_sort.append(heapq.heappop(nums))     # O(logN)
        
        return nums_sort