class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # swap tuple order -> (end_time, start_time)
        intervals = [(item[1], item[0]) for item in intervals]

        # sort by start time:
        intervals_start = sorted(intervals, key=lambda tup: tup[1])

        # initialize min heap by end time:
        min_heap_end = []
        heapq.heappush(min_heap_end, intervals_start[0])
        max_heap_size = len(min_heap_end)
        for i in range(1, len(intervals_start)):
            min_end_meeting = min_heap_end[0]
            # remove root of heap if current meeting starts after min_end_meeting ends:
            start = intervals_start[i][1]
            if start >= min_end_meeting[0]:
                heapq.heappop(min_heap_end)
            # push current meeting onto heap:
            heapq.heappush(min_heap_end, intervals_start[i])

            # update rolling max:
            if len(min_heap_end) > max_heap_size:
                max_heap_size = len(min_heap_end)
        
        return max_heap_size