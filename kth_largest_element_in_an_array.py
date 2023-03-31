import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # edge cases
        if not nums:
            return -1
        if k > len(nums):
            return -1
        
        for i in range(len(nums)): # Makes min heap to max heap #O(n)
            nums[i] = nums[i] * -1

        heapq.heapify(nums) #O(n)
        for i in range(k): #O(klogn) 
            #O(logn)
            root = heapq.heappop(nums) 
        
        return root * -1

        
        