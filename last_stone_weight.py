import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        # turn to neg
        stones = [-1 * stone for stone in stones]
        #O(N) max heap
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            if x != y:
                heapq.heappush(stones, (y-x)* -1)
        
        if len(stones) == 1:
            return stones[0] * -1
        else:
            return 0
        