s = "abcabcbb"

def solution(s):
    #sliding window with a hash map
    dic = {}
    left = 0
    right = 0
    total = 0
    temp_total = 0
    while right < len(s):
        if s[right] not in dic:
            dic[s[right]] = 1
            temp_total += 1
            right += 1
        else:
            total = max(temp_total, total)
            temp_total = 0
            left += 1
            del dic[s[left]]
    
    return total
print(solution(s))
