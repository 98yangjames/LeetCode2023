import heapq

class EventLogger:
    def __init__(self):
        self.heap = []
    def log(self, timestamp):
        self.heap.append(timestamp)

    def count_events(self,start_time, end_time):
        ans = []
        if self.heap:
            for i in self.heap:
                if i >= start_time and i <= end_time:
                    ans.append(i)
        
        return len(ans)

logger = EventLogger()

logger.log(1)
logger.log(5)
logger.log(7)
logger.log(10)

print(logger.count_events(1, 5))
