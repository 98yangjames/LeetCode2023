import heapq
# sort the list of intervals
input = [[1,3],[2,6],[8,10],[15,18]]

def merge(input):
    if len(input) == 0:
        return []
    if len(input) == 1:
        return [input[0]]
    #sorted nums
    heapq.heapify(input)
    start = input[0][0]
    end = input[0][1]
    res = []
    for x,y in input[1:]:
        if end >= x:
            end = y
        else:
            res.append([start, end])
            start = x
            end = y
    res.append([start, end])
    return res
print(merge(input))