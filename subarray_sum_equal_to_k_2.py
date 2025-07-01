#sliding window
nums = [1, 1, 1]
k = 2


def solution(nums, k):
    if len(nums) < k:
        return 0
    total = 0
    #brute force
    for i in range(len(nums)):
        temp_sum = nums[i]
        for j in range(i, len(nums)-1):
            if temp_sum + nums[j] == k:
                total += 1
            elif temp_sum + nums[j] < k:
                temp_sum = temp_sum + nums[j]
            elif temp_sum + nums[j] > k:
                break
    return total
print(solution(nums, k))