def minimumAverageDifference(nums):
    n = len(nums)
    first = 0
    second = sum(nums)
    avg_index = n // 2
    diff = 0
    current_min_avg = 0
    for i in range(n):
        first += nums[i]
        second -= nums[i]
        v1  = first // (i + 1)
        v2 = 0
        if n != (i+1):
            v2 = second // (n - (i + 1))
        diff = abs(v1 - v2)
        current_min_avg = max(current_min_avg, diff)
        if i == avg_index:
            break
    return current_min_avg
